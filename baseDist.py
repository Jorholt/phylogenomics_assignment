import math


def calculateDist(array1, array2):
	#Sanity check input
	assert len(array1) == 4 and len(array2) == 4
	#Otherwise do stuff
	result=math.sqrt( 0.25 * (math.pow(array1[0]-array2[0],2) + (math.pow(array1[0]-array2[0],2)) + ( math.pow(array1[1]-array2[1],2) ) + ( math.pow(array1[2]-array2[2],2) ) + ( math.pow(array1[3]-array2[3],2) ) ) )
	return round(result,3)

def countBases(sequence):
    assert type(sequence) is str
    a = 0
    c = 0
    g = 0
    t = 0
    for i in sequence:
        assert i in 'ACGT'
        if i == 'A':
            a+= 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1
        elif i == 'T':
            t += 1
    baselist = []
    baselist.append(a/len(sequence))
    baselist.append(c/len(sequence))
    baselist.append(g/len(sequence))
    baselist.append(t/len(sequence))

    assert abs(1 - sum(baselist)) < 0.001

    return baselist

