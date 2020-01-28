def kthNode(Root, k):
	if Root is None or k is 0:
		return None

	return kthNode1(Root,k)

def kthNode1(Root, k):
	target = None
	if Root.left is not None:
		target= kthNode1(Root.left, k)

	if target==None:
		if k==1:
			target = Root
		else:
			k= k-1 

	if Root.right is not None:
		target = kthNode1(Root.right, k)

	return target
