def serialize(Root, num):
	if Root is None:
		num.append('$')
		return 
	num.append(Root.item)

	serialize(Root.left)
	serialize(Root.right)

def deSerialize(num):
	node = None
	item = num.pop(0)

	if num[i]!='$':
		node = Node(item)
		node.left = deSerialize(num)
		node.right = deSerialize(num)
	return node