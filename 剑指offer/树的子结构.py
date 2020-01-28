class Node():
	def __init__(self,item=None,lchild=None,rchild=None):
		self.item = item
		self.lchild = lchild
		self.rchild = rchild

def hasSubTree(Node1, Node2):
	result = False

	if Node1.item != None and Node2.item != None: 
		if Node1.item == Node2.item:
			result = DoesTree(Node1,Node2)
		if not result:
			result = hasSubTree(Node1.lchild, Node2)
		if not result:
			result = hasSubTree(Node1.rchild, Node2)
	return result

def DoesTree(Node1,Node2):
	if Node2 is None:
		return True
	if Node1 is None:
		return False
	if Node1.item != Node2.item:
		return False
	return DoesTree(Node1.lchild,Node2.rchild)and DoesTree(Node1.rchild,Node2.rchild)
	