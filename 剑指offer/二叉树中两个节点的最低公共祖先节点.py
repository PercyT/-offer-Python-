def GetNodePath(Root, Node, path):
	"""用列表来存储公共区域"""
	if Root is None or Node is None:
		return False
	path.append(Root)
	if Root == Node:
		return True
	found = False
	found = GetNodePath(Root.left, Node, path)
	if !found:
		found = GetNodePath(Root.right, Node, path)
	if !found:
		path.pop()
	return found

def getLastCommonNode(path1,path2):
	small = len(path1)
	big = len(path2)
	if small>big:
		small = len(path2)
		big = len(path1)
	last = 0
	for i in range(0, small):
		if path1[i]==path2[i]:
			last = path1[i]
		else:
			break
	return last
		