class Node():
	def __init__(self, item):
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


def FindKtotail(head, k):
	second = head
	if head is None or k==0:
		return 
	for i in range(0, k-1):
		second = second.next
		if second is None:
			return
	while second.next is not None:
		head = head.next
		second = second.next
	return head.item

def PrintLinklist(head):
	while head:
		print(head.item)
		head = head.next
		
if __name__ == '__main__':
	l = [1,2,3,4,5,6]
	head = CreateLinklist(l)	
	PrintLinklist(head)		
	print(FindKtotail(head, 3))