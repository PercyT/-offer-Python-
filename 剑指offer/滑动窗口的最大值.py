def maxInwindows(num, size):
	if not num or size<=0:
		return
	maxqueue = []
	maxlist = []
	for i in range(len(num)):
		if len(maxqueue)>0 and i-size>maxqueue[0]:
			maxqueue.pop(0)
		while len(maxqueue)>0 and num[i]>num[maxqueue[-1]]:
			maxqueue.pop()
		maxqueue.append(i)
		if i >= size-1:
			maxlist.append(num[maxqueue[0]])
	return maxlist

if __name__ == '__main__':
	print(maxInwindows([2,3,4,2,6,2,5,1],3))
