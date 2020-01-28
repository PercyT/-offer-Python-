class solution():
	def MorethanHalfNum(self, num):
		dict = {}
		for i in num:
			if i in dict:
				dict[i] = dict[i] + 1
			else:
				dict[i] = 1
			if dict[i] >= len(num)/2:
				return i
		return 0

	def MorethanHalfNum2(self, num):
		result = num[0]
		times = 1
		for i in num:
			if times == 0:
				result = i
				times = 1
			elif result==i:
				times = times + 1
			else:
				times = times - 1

		times = 0
		for i in num:
			if result == i:
				times += 1
		if times*2>=len(num):
			return True
		else:
			return False

if __name__ == '__main__':
	num = [1,2,3,2,2]
	a = solution()
	print(a.MorethanHalfNum2(num))