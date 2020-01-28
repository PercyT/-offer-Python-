def findNumAppearOnce(num):
	if num is None:
		return

	result = 0
	for i in num:
		result^=i
	first = findFirstBit(result)

	a = b = 0
	for i in num:
		if isBit(i,first):
			a = a^i
		else:
			b = b^i
	return [a,b]


def findFirstBit(result):
	index = 0
	while result&1==0:
		result = result>>1
		index = index+1
	return index

def isBit(i, first):
	i = i>>first
	if i&1==1:
		return True
	else:
		return False
