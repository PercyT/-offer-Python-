def findContinuousSequence(sum):
	if sum<3:
		return

	small = 1
	big = 2
	mid = (1+sum)/2
	cursum = small+big
	while small<mid:
		if cursum==sum:
			printk(small,big)
		while cursum>sum and small<mid:
			cursum -= small
			small += 1
			if cursum==sum:
				printk(small,big)
		big += 1
		cursum += big

def printk(small,big):
	for i in range(small, big+1):
		print(i,end=' ')

