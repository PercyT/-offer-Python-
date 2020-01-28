def numberOf1(num):
	ints = list(str(num))
	first = int(ints[0])
	length = len(ints)
	if length == 1 and first ==0:
		return 0
	if length == 1 and first >0:
		return 1

	num_first_digit = 0
	if first>1:
		num_first_digit = powerBase10(length-1)
	if first == 1:
		










if __name__ == '__main__':
	