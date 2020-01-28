class node():
	def __init__(self,item):
		self.item = item
		self.next = None

def createLinkList(l:list)->node:
	"""创建一个链表"""
	if not l:
		return
	head = node(l[0])
	p = head
	for i in l[1:]:
		p.next = node(i)
		p = p.next
	return head

def reversePrintLinkList(head):
	"""使用栈来存储遍历链表而得的值"""
	if not head:
		return
	stack = []
	while head:
		stack.append(head.item)
		head = head.next
	for i in stack[::-1]:
		print(i)

def reversePrintLinkList2(head):
	"""使用递归来实现，递归在本质上就是一个栈结构"""
	if not head:
		return
	if head.next:
		reversePrintLinkList2(head.next)	
	print(head.item)	

if __name__ == '__main__':
	l = [1,2,3,4,5]
	head = createLinkList(l)
	reversePrintLinkList(head)
	reversePrintLinkList2(head)

