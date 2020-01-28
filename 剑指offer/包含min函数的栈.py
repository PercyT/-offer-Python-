class Min_stack():
	def __init__(self):
		self.stack = []
		self.min_stack = []

	def push(self, item):
		self.stack.append(item)
		if self.min_stack:
			if item<self.min():
				self.min_stack.append(item)
			else:
				self.min_stack.append(self.min())
		else:
			self.min_stack.append(item)

	def pop(self):
		if stack is []:
			return
		data = self.stack.pop()
		self.min_stack.pop()
		return data

	def min(self):
		if stack is []:
			print('stack is empty')
		else:
			return self.min_stack[-1]

if __name__ == '__main__':
	stack = Min_stack()
	stack.push(1)
	stack.push(2)
	stack.push(0)
	print(stack.min())
	stack.pop()
	print(stack.min())