class Node(object):
	def __init__(self, item):
		self.item = item
		self.next = None
	def __del__(self):
		self.item = None
		self.next = None

def createLinkList(l:list)->Node:
	"""创建一个链表"""
	if not l:
		return
	head = Node(l[0])
	p = head
	for i in l[1:]:
		p.next = Node(i)
		p = p.next
	return head

def deleteNode(head, node):
	"""删除链表节点"""
	if head is node and node.next is None:
		head.__del__()
	elif node.next is None:
		while head.next is not node:
			head = head.next
		head.next = None
	else:
		node.item = node.next.item
		node.next = node.next.next

def deleteRepeat(head):
	first = Node(-1)	
	first.next = head
	last = first # 表示上一个遍历的节点
	while head and head.next:
		if head.item==head.next.item:
			item = head.item
			while head and head.item==item:
				head = head.next
			last.next = head  # 把下一个不重复的节点赋值
		else:
			last = head
			head = head.next
	return first.next

def printLinklist(head):
	while head:
		print(head.item)
		head = head.next
if __name__ == '__main__':
	l = [1,2,2,2,3,3,4]
	head = createLinkList(l)
	head = deleteRepeat(head)
	# deleteNode(head, head)
	printLinklist(head)


