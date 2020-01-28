def theMin(num:list)->int:
	if num is None:
		return 
	start = 0
	end = len(num)-1
	mid = start
	while num[start]>=num[end]:
		if (end - start)==1:
			mid = end
			break
		mid = (start+end)//2
		if num[start] == num[end] and num[mid] == num[end]:
			return MinOrder(num,start,end)
		if num[mid]>=num[start]:
			start = mid
		elif num[mid]<=num[end]:
			end = mid
	return num[mid]

def MinOrder(num,start,end):
	result = num[start]
	for i in num:
		if i < result:
			result = i
	return result
num = [1,0,1,1,1]
print(theMin(num))
  