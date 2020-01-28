def getStr(num):
	# f(n)表示的是第n+1位上可能存在的情况，赋给初值f(n) = 1 进行递归
	string = list(str(num))
	n = len(string) - 1
	f = [0 for i in range(0, len(string))]
	f[n] = 1

	for i in range(n-1,-1,-1):
		if i == n-1:
			f[i] = f[i+1] + g(string,i)*1
		else:
			f[i] = f[i+1] + g(string,i)*f[i+2]
	return f[0]

def g(string, i):
	num = int(string[i] + string[i+1])
	if num>=10 and num<=25:
		return 1
	else:
		return 0

if __name__ == '__main__':
	print(getStr(12258))