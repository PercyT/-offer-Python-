def getUglyNumber(index):
	if index<0:
		return
	uglyNum = [0 for i in range(index)]
	uglyNum[0] = 1                                                                                                                                                                                                                                                                                                                
	p2 = 0
	p3 = 0
	p5 = 0
	nextUglyIndex = 1
	while nextUglyIndex<index:
		minnum = min(uglyNum[p2]*2,uglyNum[p3]*3,uglyNum[p5]*5)
		uglyNum[nextUglyIndex] = minnum
		while uglyNum[nextUglyIndex]>=uglyNum[p2]*2:
			p2 = p2+1
		while uglyNum[nextUglyIndex]>=uglyNum[p3]*3:
			p3 = p3+1
		while uglyNum[nextUglyIndex]>= uglyNum[p5]*5:
			p5 = p5+1
		nextUglyIndex = nextUglyIndex+1

	return uglyNum

if __name__ == '__main__':
	print(getUglyNumber(20))