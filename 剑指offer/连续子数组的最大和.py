def FindLargest(num):
	"""还可以用动态规划法，算法差不多"""
	currentSum = 0
	max = 0
	for i in num:
		currentSum += i
		if currentSum<0:
			currentSum = 0
		if currentSum>max:
			max = currentSum
	return max





if __name__ == '__main__':
	print(FindLargest([1,2,-3,-4,5]))