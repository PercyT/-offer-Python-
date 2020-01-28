def yuesefuhuang(n, m):
	if n<1 or m<1:
		return

	last = 0
	for i in range(2, n+1):
		last = (last+m)%i

	return last