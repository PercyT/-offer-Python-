class Node():
	def __init__(self, item):
		self.item = item
		self.next = None
		self.sibling = None

def cloneNodes(head):
	node = head
	while node is not None:
		new = Node()
		new.item = node.item
		new.next = node.next
		node.next = new

		node = new.next

def connectSibingNodes(head):
	node = head
	while node is not None:
		clone = node.next
		if node.sibling is not None:
			clone.sibling = node.sibling.next

		node = clone.next

def connectToTwoLinklist(head):
	node = head
	oldHead = head
	newHead = head.next
	newNode = node.next

	while newNode.next is not None:	
		node.next = newNode.next
		newNode.next = node.next.next

		node = node.next
		newNode = newNode.next
	return newHead


if __name__ == '__main__':
	cloneNodes(head)
	connectSibingNodes(head)
	connectToTwoLinklist(head)

