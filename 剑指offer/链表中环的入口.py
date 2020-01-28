class Node():
	def __init__(self,item):
		self.item = item
		self.next = None

def CreateLinklist(l):
	if l is None:
		head = None
		return head
	head = Node(l[0])
	p = head
	for i in l[1:]:
		p.next = Node(i)
		p = p.next
	return head

def meetingNode(head):
	if head is None:
		return

	slow = head
	fast = slow.next
	while slow and fast:
		if slow==fast:
			return fast
		slow = slow.next
		fast = fast.next
		if fast.next:
			fast = fast.next
	return None

def EntryNodeofLoop(head):
	meetNode = meetingNode(head)
	if meetingNode is None:
		return
	# 得到环的节点数量
	num = 1
	pnode = meetingNode
	while pnode.next is not meetingNode:
		pnode = pnode.next
		num += 1

	first = head
	second = head
	for i in range(0, num):
		first = first.next
	while first != second:
		first = first.next
		second = second.next
	return first
