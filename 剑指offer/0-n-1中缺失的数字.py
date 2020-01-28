def GetMissingNum(num):
	left = 0
	right = len(num)-1
	while left<right:
		mid = (left+right)//2
		if num[mid]!=mid:
			if num[mid-1]==mid-1 or mid = 0:
				return mid
			right = mid-1
		else:
			left = mid+1
	return -1

