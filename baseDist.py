import math
import argparse

def calculateDist(array1, array2):
	#Sanity check input
	assert len(array1) == 4 and len(array2) == 4
	#Otherwise do stuff
	result=math.sqrt( 0.25 * (math.pow(array1[0]-array2[0],2) + (math.pow(array1[1]-array2[1],2)) + ( math.pow(array1[2]-array2[2],2) ) + ( math.pow(array1[3]-array2[3],2) ) ) )
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

	assert abs(1 - sum(baselist)) < 0.001 			#Does not work in python 2.7~ append?

	return baselist

def printMatrix(matrix):
	for row in matrix:
		if len(row[0]) > 10:
			row[0]=row[0][0:10]
		elif len(row[0]) < 10:
			row[0]=row[0]+' '*(10-len(row[0])) #Check if name is shorter than 10 characters, in that case add 10-len(row[0]) number of ' ' characters
		for i in range(0,len(row)):
			outputString = "%s\t" % (row[i])
			print(outputString) 

#-------------------------main---------------------
parser = argparse.ArgumentParser(description='Process list of files.')
parser.add_argument('files', type=str, nargs='+',
                    help='filenames')
args = parser.parse_args()
print(args.files)

sequenceData=[]
for i in args.files:
	sequence = file_to_seq(i)
	nucleotideComposition=countBases(sequence[1])
	sequencedata.append([sequence[0],sequence[1],nucleotideComposition])

matrix=[]
for y in sequenceData:
	row=[]
	row.append(y[0])
	for x in sequenceData:
		row.append(calculateDist(y[2],x[2]))
	matrix.append(row)

printMatrix(matrix)