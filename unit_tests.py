from baseDist import *

def test1():
	testArray1	=	[0.25, 0.25, 0.25, 0.25]
	testArray2	=	[0.2, 0.2, 0.3, 0.3]
	obs = calculateDist(testArray1, testArray2)
	exp = 0.05
	assert obs == exp

def test2():
	testSequence1='AAGFTTCC'
	obs=countBases(testSequence1)	
	exp=NotImplemented
	assert obs==exp
	
def test3():
	fakematrix=[["namn1",0.04,0.04,0.04,0.04,0.04,0.04,0.04],["namn2",0.03,0.03,0.03,0.03,0.03,0.03,0.03]]
	printMatrix(fakematrix)