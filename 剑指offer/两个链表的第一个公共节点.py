def getListLength(head):
	num = 0
	while head:
		num += 1
		head = head.next

def findFirstCommonNode(head1, head2):
	length1 = getListLength(head1)
	length2 = getListLength(head2)
	dif = length1-length2
	long = head1
	short = head2
	if length2>length1:
		dif = length2-length1
		long = head2
		short = head1

	for i in range(0, dif):
		long = long.next

	while long and long.item!=short.item:
		long = long.next
		short = short.next

	FirstCommonNode = long
	return long
		
