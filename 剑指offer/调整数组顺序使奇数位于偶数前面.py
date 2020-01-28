def reorderList(num):
	if num is None:
		return 
	first = 0
	second = len(num)-1
	while first<second:
		if num[first]%2==1:
			first += 1
		if num[second]%2==0:
			second -= 1
		if num[first]%2==0 and num[second]%2==1 and first<second:
			num[first],num[second] = num[second],num[first]
num = [1,2,3,4,5,8,4]
reorderList(num)
print(num)