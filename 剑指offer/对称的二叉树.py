def isSymmetrical(root1,root2=None):
	if root2 is None:
		return isSymmetrical(root1,root1)

	if root1==None and root2==None:
		return True
	if root1==None or root2==None:
		return False
	if root1.item!=root2.item:
		return False

	return isSymmetrical(root1.lchild,root2.rchild)/ 
		and isSymmetrical(root1.rchild,root2.lchild)