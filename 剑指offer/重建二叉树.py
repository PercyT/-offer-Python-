class Node():
	def __init__(self,item=None,lchild=None,rchild=None):
		self.item = item
		self.lchild = lchild
		self.rchild = rchild

class Tree():
	def __init__(self, root=None):
		self.root = root
		self.l = []      # 定义一个列表用于存储节点位置

	def preOrderTraversal(self, root):
		if root == None:
			return 
		else:
			print(root.item, end=' ')
			self.preOrderTraversal(root.lchild)
			self.preOrderTraversal(root.rchild)

	def inOrderTraversal(self, root):
		if root == None:
			return
		else:
			self.inOrderTraversal(root.lchild)
			print(root.item, end=' ')
			self.inOrderTraversal(root.rchild)


def constructTree(preOrder:list, inOrder:list)->Node:
	if not preOrder or not inOrder or (len(preOrder)!=len(inOrder)):
		return

	def construct(preOrder, inOrder):
		if not preOrder:
			return None
		root = Node(preOrder[0])
		for i,j in enumerate(inOrder):
			if j == root.item:
				break
		root.lchild = construct(preOrder[1:1+i],inOrder[:i])
		root.rchild = construct(preOrder[1+i:],inOrder[i+1:])
		return root

	return construct(preOrder,inOrder)

if __name__ == '__main__':
	pre = [1, 2, 4, 7, 3, 5, 6, 8]
	ino = [4, 7, 2, 1, 5, 3, 8, 6]
	root = constructTree(pre,ino)
	tree = Tree(root)
	tree.preOrderTraversal(tree.root)
	print('\n')
	tree.inOrderTraversal(tree.root)
