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
	return 

def PrintLinklist(head):
	while head:
		print(head.item)
		head = head.next

def merge(head1,head2):
	if head1 is None:
		return head2
	elif head2 is None:
		return head1

	head = None
	if head1.item > head2.item:
		head = head2
		head.next = merge(head1,head2.next)
	else:
		head = head1
		head.next = merge(head1.next,head2)
	return head

if __name__ == '__main__':
	l1 = [1,3,5,7,9]
	l2 = [2,4,6,8,10]
	head1 = CreateLinklist(l1)
	head2 = CreateLinklist(l2)
	head = merge(head1,head2)
	PrintLinklist(head)