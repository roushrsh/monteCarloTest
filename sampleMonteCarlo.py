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
import scipy.stats
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



def forcedMonteCarlo(numSimulations, lowerBoundThickness, upperBoundThickness, strengthMean, strengthSD):
	average = 0
	
	for i in range(numSimulations):
		randomThickness = uniformDistribution(lowerBoundThickness,upperBoundThickness)
		randomStrength = getNormalDistribution(strengthMean,strengthSD)
		area = forceCalculation(randomThickness, randomStrength)
		average = average+area
	return (average / float(numSimulations))

print (forcedMonteCarlo(10000000, 50.0, 51.0, 400.0, 10.0))
