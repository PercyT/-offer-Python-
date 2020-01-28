def Power(base, exponent):
	is_wrong = False
	if base == 0 and exponent<0:
		is_wrong = True
		return 0
	if exponent == 0:
		return 1
	if exponent < 0:
		return 1/caculate(base, abs(exponent))
	return caculate(base,exponent)


def caculate(base, exponent):
	flag = base
	for i in range(1, exponent):
		flag = flag*base
	return flag

def PowerWithQuckly(base, exponent):
	if exponent ==0:
		return 1
	if exponent ==1:
		return base
	result = PowerWithQuckly(base, exponent>>1)
	result*=result
	if exponent&1==1:
		result *= base
	return result

if __name__ == '__main__':
	print(Power(2,0))
	print(PowerWithQuckly(2,5))