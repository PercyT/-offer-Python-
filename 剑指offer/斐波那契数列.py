def Fibonacci(n:int)->int:
	"""使用递归的算法计算"""
	if n <=0:
		return 0
	if n ==1:
		return 1
	return Fibonacci(n-1)+Fibonacci(n-2)

def fibonacci(n:int)->int:
	"""使用循环的方法计算"""
	first = 0
	second = 1
	for i in range(2,n+1):
		temp = first
		first = second
		second = temp+second
	return second 
print(fibonacci(5))
print(Fibonacci(5))