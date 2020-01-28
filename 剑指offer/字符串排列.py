import copy
def permutation(before):
	if before is None:
		return 
	out = []
	begin = 0
	permutation1(before, out ,begin)
	return out

def permutation1(before, out, begin):
	if begin == len(before) - 1:
		out.append(before[:]) # 或者 append(before[:])
	else:
		for i in range(begin, len(before)):
			before[i],before[begin] = before[begin],before[i]
			permutation1(before, out, begin+1)
			before[i],before[begin] = before[begin],before[i]	

if __name__ == '__main__':
	print(permutation([1,2,3,4]))












