import baseDist.py *

def test1():
	testArray1 = [0.25, 0.25, 0.25, 0.25]
  testArray2 = [0.2, 0.2, 0.3, 0.3]
	obs = calculateDist(testArray1, testArray2)
	exp = 0.05
	assert obs == exp
	
	