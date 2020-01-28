from heapq import *



class Solution(object):
	# 如果是奇数，先进入最小堆，再取最小堆最小的进入最大堆
	# 如果是偶数，先进入最大堆，再取最大堆最大的进入最小堆
	def __init__(self):
		self.small = []
		self.large = []

	def insert(self, num):
		small = self.small
		large = self.large

		if len(small)>len(large):
			heappush(small, num)
			heappush(large, -(heappop(small)))
		else:
			heappush(large, -num)
			heappush(small, -(heappop(large)))

	def getMiddle(self):
		small = self.small
		large = self.large
		if len(small)>len(large):
			return small[0]
		else:
			return (small[0]+(-large[0]))/2

if __name__ == '__main__':
	num = [1,2,3,4,5,6]
	s = Solution()
	for i in num:
		s.insert(i)

	print(s.getMiddle())
		