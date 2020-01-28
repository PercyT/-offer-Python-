def PrintToMaxOfDigits(n):
	if n<=0:
		return -1
	listNum = ['0']*n
	while Increament(listNum) is False:
		PrintNumber(listNum)

def Increament(number):
	isoverFlow = False # 溢出标志位
	isTakeOver = 0     # 进位标志位

	length = len(number)
	n = length-1
	while n>=0:
		nsum = int(number[n])+isTakeOver
		if n==length-1:
			nsum += 1
		if nsum==10:
			if n==0:
				isoverFlow = True
				return isoverFlow
			else:
				isTakeOver = 1
				number[n] = '0'
		else:
			number[n] = str(nsum)
			break
		n -= 1
	return isoverFlow

def PrintNumber(number):
	m = 0
	while number[m] == '0':
		m += 1
		if m==len(number):
			break
	print(''.join(number[m:]))


def diguiStart(n):
	if n<=0:
		return
	listNum = ['0']*n
	for i in range(0, 10):
		listNum[0] = str(i)
		digui(listNum, 0)

def digui(listNum, index):
	if index == len(listNum)-1:
		PrintNumber(listNum)
		return
	for i in range(0, 10):
		listNum[index+1] = str(i)
		digui(listNum, index+1)

if __name__ == '__main__':
	# PrintToMaxOfDigits(3)
	diguiStart(3)