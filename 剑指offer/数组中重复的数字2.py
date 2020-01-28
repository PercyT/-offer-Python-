def countRange(num, length, start, end):  # 找出在start到end区间的
	count = 0
	for i in num:
		if i>=start and i<=end:
			count += 1
	return count

def getDuplication(num, length):
	start = 1
	end = length-1
	while end>=start:
		middle = (start+end)//2
		count = countRange(num, length, start, middle)
		if start == end:
			if count>1:
				return start
			else:
				break
		if count>(middle-start+1):
			end = middle
		else:
			start = middle+1
	return -1

num = [2,3,5,4,3,2,6,7]
print(getDuplication(num,len(num)))