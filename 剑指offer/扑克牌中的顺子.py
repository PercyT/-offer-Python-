def isContinuous(num):
	if num is None:
		return
	num.sort()
	time0 = 0
	for i in num:
		if i==0:
			time0 += 1

	space = 0
	small = time0
	big = small + 1
	while  big<len(num):
		if num[small]==num[big]:
			return False
		space = num[big]-num[small]-1
		small = big
		big += 1
	if time0>=space:
		return True
	else:
		return False


if __name__ == '__main__':
	print(isContinuous([1,2,3,4,5]))