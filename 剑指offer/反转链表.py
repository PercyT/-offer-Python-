class node():
	def __init__(self, item):
		self.item = item
		self.next = None

def createLinkList(l):
	"""创建一个链表"""
	if not l:
		return
	head = node(l[0])
	p = head
	for i in l[1:]:
		p.next = node(i)
		p = p.next
	return head

def PrintLinklist(head):
	while head:
		print(head.item)
		head = head.next

def reverseLinklist(head):
	pre = None
	pnode = head
	reverseNode = None
	while pnode is not None:
		pnext = pnode.next
		pnode.next = pre
		pre = pnode
		pnode = pnext
	reverseNode = pre
	return reverseNode

if __name__ == '__main__':
	l = [1,2,3,4,5]
	head = createLinkList(l)
	reverse = reverseLinklist(head)
	PrintLinklist(reverse)