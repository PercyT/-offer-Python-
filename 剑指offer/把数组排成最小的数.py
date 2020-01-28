from operator import lt

def printMinNumber(num):
	# num = [3,32,321] 引入一个新的排序规则，对快速排序算法进行改进
	if not num:
		return ''
	num = list(map(str, num))
	pivot = num[0]

	left = [i for i in num[1:] if (pivot+i)>(i+pivot)]
	right = [i for i in num[1:] if (i+pivot)>(pivot+i)]
	return ''.join(printMinNumber(left)) + pivot + ''.join(printMinNumber(right))


def printMinNumber1(num):
	num = list(map(str, num))
	left = 0
	right = len(num)-1
	quickSort(num, left, right)
	print(num)

def quickSort(input, left, right):
	if left<right:
		index = getIndex(input, left, right)
		quickSort(input, left, index)
		quickSort(input, index+1, right)

def getIndex(input, left, right):
	p = input[left]
	while left<right:
		while p+input[right]<input[right]+p and left<right:
			right -= 1
		input[left] = input[right]
		while p+input[right]>input[right]+p and left<right:
			left += 1
		input[right] = input[left]
	input[left] = p
	return left


if __name__ == '__main__':
	print(printMinNumber1([3,32,321]))