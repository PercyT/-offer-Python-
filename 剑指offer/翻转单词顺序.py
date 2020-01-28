def reverseSentance(s):
	if s is None or s == '':
		return

	s1 = s[::-1]

	l = 0
	r = s1.index(" ")

	ans = ''
	while r<len(s1):
		ans += s1[l:r][::-1] + " "
		l = r+1
		r = r+1

		while r<len(s1) and s1[r]!=' ':
			r = r+1
	# ans += s1[l: r][::-1]
	return ans

if __name__ == '__main__':
	print(reverseSentance('i am'))
