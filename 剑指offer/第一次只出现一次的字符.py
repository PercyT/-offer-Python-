def findOneAppear(string):
	map = {}
	for i in string:
		if i not in map:
			map[i] = 1
		else:
			map[i] += 1

	for key,value in map.items():
		if value == 1:
			print(key,end = ' ')


if __name__ == '__main__':
	findOneAppear('abaccdeff')