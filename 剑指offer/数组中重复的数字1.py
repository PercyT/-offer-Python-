def duplicate(num):
	for i,v in enumerate(num): # 关键在于数字如果是i那么他的数组下标一定是i
		while num[i] != i:
			if num[v] == v:
				return True
			num[i],num[v] = num[v],num[i] # 将两个交换，使得num[v]肯定满足数组下标等于数字 
	return False

num = [0,1,2,2]
print(duplicate(num))