#Sample Monte Carlo test to practice

#I asked a Civil Engineer friend for a problem he'd encounter in his work, and I attempted to solve it myself using Monte Carlo simulation.
#Example from structural engineering, Engineer needs to find tensile strength of a steel bar from a manufacturer
#equation is area * material strength = max force
#There are manufacturing methods/error. Perhaps diameter of the bar can be expressed as a uniform random variable between 50 and 51 mm
#Material strength can probably be considered to be normally distributed, ex: mean of 400MPa, and standard deviation of 10MPa
#You could calculate analytically, exactly what the distribution of the max force will be.
#But for more complex models with many random variables, it becomes easier to just do a million simulations and see the distributionan at the end

#He's going to do it how he does it at work using excel, while I code it, and we compare results.
'''
How I'm approaching it, we have two unknown, one is the uniform dist from 50 to 51 mm. 
Other is unknown of 400MPa, which I'll have to do a normally distributed deviation of 10 MPa
Formula for cylinder ia A=pi*D^2/4
That's in mm^2, Material strength is in MPa=N/mm^2
So result will be in Newtwons
'''
import numpy as np
import math
import random
from matplotlib import pyplot as plt

from IPython.display import clear_output

#For pi I will use math.pi and math.exp(x) for e
#I will use numpy to get normalDistributionGuess


def forceCalculation(thickness, strength):
	#area * strength will give the force
	area = ((math.pi)*float(thickness)*(thickness)/4.0) * strength[0]
	return area

def getNormalDistribution(mean, standardD):
	randomValue = np.random.normal(mean, standardD, 1)
	return randomValue
	

def uniformDistribution(minValue, maxValue):
	"""
		Gets a random number from a uniform distribution between the two values.
		Floats given, returns a float
	"""
	uniD = random.uniform(minValue,maxValue)
	return uniD




def monteCarlo(numSimulations, lowerBoundThickness, upperBoundThickness, strengthMean, strengthSD):
	average = 0
	
	for i in range(numSimulations):
		randomThickness = uniformDistribution(lowerBoundThickness,upperBoundThickness)
		randomStrength = getNormalDistribution(strengthMean,strengthSD)
		force = forceCalculation(randomThickness, randomStrength)
		average = average+force
	return (average / float(numSimulations))

print (monteCarlo(100000, 50.0, 51.0, 400.0, 10.0))



#What if we want to know the variance?
#well we can get that too, now that we have the mean, we can rerun it.
#Variance is the sum of (x-mean)^2/(N-1). We're using N-1 instead of N because our data is a sample instead of the whole population
#we will have to change our code to store the random thickness and strength for accurate variation.
#We will also need new methods to have arrays stored


def getNDArray(mean, standardD, numSimulations):
	randomValueArray = np.random.normal(mean, standardD, numSimulations)
	return randomValueArray

def getUDArray(minValue, maxValue, numSimulations):
	randomValueArray = np.random.uniform(minValue, maxValue, numSimulations)
	return randomValueArray


def getForceArray(thickness, strength):
	#area * strength will give the force
	area = ((math.pi)*(thickness)*(thickness)/4.0) * strength
	return area

#Variance is sum((x-mean)²)/(N-1)

def monteCarloVariance(numSimulations, lowerBoundThickness, upperBoundThickness, strengthMean, strengthSD):
	randomThicknessArray = getUDArray(lowerBoundThickness,upperBoundThickness,numSimulations)
	randomStrengthArray = getNDArray(strengthMean,strengthSD,numSimulations)
	forceArray = getForceArray(randomThicknessArray, randomStrengthArray)
	meanOfForce = (np.mean(forceArray))  #What we were calculating before!
	varianceGrid = ((forceArray - meanOfForce))
	varianceGridSquared = varianceGrid * varianceGrid
	sumOfIt = np.sum(varianceGridSquared)
	variance = sumOfIt/(numSimulations-1) #as we're sampling a populaiton, not the whole


	##other way
	average = 0
	squareOfAverage =0
	for i in range(numSimulations):
		randomThickness = uniformDistribution(lowerBoundThickness,upperBoundThickness)
		randomStrength = getNormalDistribution(strengthMean,strengthSD)
		force = forceCalculation(randomThickness, randomStrength)
		average = average+force
		squareOfAverage = squareOfAverage + force * force

	squareOfMean = (average/numSimulations)**2
	meanOfSquares = squareOfAverage/numSimulations
	methodTwoVariance =  (meanOfSquares - squareOfMean)

	return (variance, methodTwoVariance)

variance = (monteCarloVariance(100000, 50.0, 51.0, 400.0, 10.0))


print (variance)
#Also can get standard deviation which is square root of it
sd = np.sqrt(variance)
print (sd)




