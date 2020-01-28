class Solution():
	def __init__(self):
		self.linkHead = None
		self.linkTail = None

	def convert(self, root):
		if root is None:
			return

		self.convert(root.left)
		if self.linkHead is None:
			self.linkHead = root
			self.linkTail = root
		else:
			self.linkTail.right = root
			root.left = self.linkTail
			self.linkTail = root
		self.convert(root.right)
		return self.linkHead

