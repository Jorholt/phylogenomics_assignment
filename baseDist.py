import math

def calculateDist(array1, array2):
	#Sanity check input
	assert len(array1) == 4 and len(array2) == 4
	#Otherwise do stuff
	result=math.sqrt( 0.25 * (math.pow(array1[0]-array2[0],2) + (math.pow(array1[0]-array2[0],2)) + ( math.pow(array1[1]-array2[1],2) ) + ( math.pow(array1[2]-array2[2],2) ) + ( math.pow(array1[3]-array2[3],2) ) ) )
	return round(result,3)
