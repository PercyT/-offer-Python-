def countOfInt(n):
	if n == 1:
		return 10
	else:
		count = 10**(n-1)
		return 9*count

def beginNumber(n):
	if n == 1:
		return 0
	return 10**(n-1)

def digit(index):
	if index<0:
		return

	n = 1
	while True:
		count = countOfInt(n)
		if index<count*n:
			return digitFind(index, n)
		index -= count*n
		n += 1

def digitFind(index, n):
	div, mod = divmod(index, n)
	begin = beginNumber(n)
	num = begin + div
	mod = n-mod
	for i in range(1, mod):
		num = num//10
	return num%10


if __name__ == '__main__':
	print(digit(19))