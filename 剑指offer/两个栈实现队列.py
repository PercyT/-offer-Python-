class Queue():
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def add(self, value):
		self.stack1.append(value)
		print('{} is added to the Queue'.format(value))

	def delete(self):
		if self.stack2:
			v = self.stack2.pop()
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			if not self.stack2:
				print('Queue is empty!')
			v = self.stack2.pop()	
		print('{} is removed from the Queue'.format(v))

if __name__ == '__main__':
	queue = Queue()
	for i in [1,2,3]:
		queue.add(i)
	queue.delete()