def printFromToptoBottom(Root):
	queue = []
	if Root is None:
		return 

	queue.append(Root)
	while queue:
		Node = queue[-1]
		print(queue.pop(0).item)

		if Node.left:
			queue.append(Node.left)

		if Node.right:
			queue.append(Node.right)
		
def printFromToptoBottom2(Root):
	"""分行打印"""
	printlist = []
	curlist = [Root]

	while curlist:
		list1 = []
		nextlist = []
		for i in range(curlist):
			list1.append(i.item)
			if i.left:
				nextlist.append(i.left)
			if i.right:
				nextlist.append(i.right)
		printlist.append(list1)
		curlist = nextlist
	return printlist

def printFromToptoBottom3(Root):
	"""偶数层交叉访问"""
	printlist = []
	curlist = [Root]
	isEven = True

	while curlist:
		list1 = []
		nextlist = []
		isEven = not isEven
		for i in range(curlist):
			list1.append(i.item)
			if i.left:
				nextlist.append(i.left)
			if i.right:
				nextlist.append(i.right)
		printlist.append(list1[::-1]) if isEven else printlist.append(list1)
		curlist = nextlist

	return printlist