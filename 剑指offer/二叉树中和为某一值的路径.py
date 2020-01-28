def init(Root, expectedSum):
	if Root is None:
		return
	path = []
	currentSum = 0
	FindBath(Root, expectedSum, path, currentSum)

def FindBath(Root, expectedSum, path, currentSum):
	currentSum = currentSum + Root.item
	path.append(Root.item)
	isleaf = True if Root.left is None and Root.right is None else isleaf = False
	if currentSum == expectedSum and isleaf:
		print("finded path is:")
		for i in path:
			print(i,end=' ')

	if Root.left:
		FindBath(Root.left, expectedSum, path, currentSum)
	if Root.right:
		FindBath(Root.right, expectedSum, path, currentSum)
	path.pop()


