def findNumwithSum(num, sum):
	first = 0
	two = len(num)-1
	while two>first:
		cursum = num[first]+num[two]
		if cursum==sum:
			return (num[first],num[two])
		elif cursum>sum:
			two -= 1
		else:
			first += 1

if __name__ == '__main__':
	a,b = findNumwithSum([1,2,4,7,11,15],15)
	print("{} {}".format(a,b))