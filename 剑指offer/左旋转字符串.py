def leftRotateString(string, n):
	pleft = 0
	pleftend = n-1
	pright = n
	prightend = len(string) - 1
	s = list(string)
	print(s)
	reverse1(s, pleft, pleftend)
	reverse1(s, pright, prightend)
	reverse1(s, pleft, prightend)
	return ''.join(s)

def reverse1(s, start, end):
	while start<end:
		s[start],s[end] = s[end],s[start]
		start = start + 1
		end = end - 1


if __name__ == '__main__':
	A = 'abcdefg'
	s = leftRotateString(A, 2)
	print(s)