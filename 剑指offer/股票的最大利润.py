def maxDiff(num):
	maxDiff = 0
	currentDiff = 0
	min = num[0]

	for i in range(1, len(num)):
		currentDiff = num[i]-min
		if num[i]<min:
			min = num[i]
		if currentDiff>maxDiff:
			maxDiff = currentDiff

	return maxDiff

if __name__ == '__main__':
	print(maxDiff([9,11,8,5,7,12,16,14]))