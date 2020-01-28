class Node():
	def __init__(self,item=None,lchild=None,rchild=None):
		self.item = item
		self.lchild = lchild
		self.rchild = rchild

def Mirror(Node):
	if Node is None:
		return
	if Node.lchild is None and Node.rchild is None:
		return 
	Node.lchild,Node.rchild = Node.rchild,Node.lchild
	if Node.lchild:
		Mirror(Node.lchild)
	if Node.rchild:
		Mirror(Node.rchild)