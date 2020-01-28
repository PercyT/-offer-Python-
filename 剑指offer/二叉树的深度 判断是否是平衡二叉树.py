def treeDeepth(Root):
	"""计算树的深度"""
	if Root is None:
		return 0
	left = treeDeepth(Root.left)
	right = treeDeepth(Root.right)

	return left+1 if left>right else right+1

def isBalanced(Root, deepth):
	"""判断是否是平衡二叉树"""
	if Root is None:
		deepth = 0
		return True,deepth

	is1, left = isBalanced(Root.left, deepth)
	is2, right = isBalanced(Root.right, deepth)

	if is1 and is2:
		if left-right<-1 or left-right>1:
			return False,deepth
		else:
			deepth = left+1 if left>right else right+1
			return True,deepth
	return False,deepth
