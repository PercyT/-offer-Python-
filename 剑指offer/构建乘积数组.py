def multiply(A):
	n = len(A)
	B = [0]*n
	B[0] = 1
	for i in range(1, n):
		B[i] = B[i-1]*A[i-1]
	temp = 1
	for j in range(n-2,-1,-1):
		temp *= A[j+1]
		B[j] *= temp
	return B

if __name__ == '__main__':
	print(multiply([1,2,3,4]))