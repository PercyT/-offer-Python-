class Node():
	def __init__(self,item=None,lchild=None,rchild=None,parent=None):
		self.item = item
		self.lchild = lchild
		self.rchild = rchild
		self.parent = parent

def getNext(node):
	if node is None:
		return 
	if node.rchild:
		node = node.rchild
		while node.lchild:
			node = node.lchild
		return node
	else:
		while node.parent:
			if node.parent.lchild==node:
				return node.parent
			node = node.parent


