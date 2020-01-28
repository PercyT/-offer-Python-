def FindOneNumber(num):
	one = 0
	two = 0
	three = 0
	for i in num:
		two = two|(one&i)
		one = one^i
		three = one&two
		one = one&(~three)
		two = two&(~three)
	return one
