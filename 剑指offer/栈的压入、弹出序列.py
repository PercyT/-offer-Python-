def isPopOrder(push:list, pop:list):
	stack = []
	j = 0
	for i in push:
		stack.append(i)
		while stack and stack[-1]==pop[j]:
			stack.pop()
			j = j + 1

	return stack == []

if __name__ == '__main__':
	push = [1,2,3,4,5]
	pop = [4,5,3,2,1]
	print(isPopOrder(push,pop))

