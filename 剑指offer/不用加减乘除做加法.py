def add(num1, num2):
	while True:
		sum = num1^num2
		carry = (num1&num2)<<1
		num1 = sum
		num2 = carry
		if carry==0:
			return num1

if __name__ == '__main__':
	print(add(1,166))
		