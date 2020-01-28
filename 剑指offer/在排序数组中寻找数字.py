def getFirstK(num, k, start, end):
	if end<start:
		return

	mid = (start+end)//2
	if num[mid] == k:
		if (num[mid-1]!=k and mid>0) or mid == 0:
			return mid
		else:
			end = mid-1
	elif num[mid] >k:
		end = mid-1
	else:
		start = mid + 1

	return getFirstK(num,k,start,end)

def getLastK(num, k ,start, end):
	if end<start:
		return

	mid = (start+end)//2
	if num[mid] == k:
		if  mid==end or (num[mid+1]!=k and mid<end):
			return mid
		else:
			start = mid + 1
	elif num[mid] <k:
		start = mid+1
	else:
		end = mid-1

	return getLastK(num,k,start,end)

def getNumberofK(k, num):
	if not num :
		return
	first = getFirstK(num,k,0,len(num)-1)
	last = getLastK(num,k,0,len(num)-1)
	print(first)
	print(last)
	if first>-1 and last>-1:
		return last-first+1

if __name__ == '__main__':
	print(getNumberofK(3,[1,2,3,3,3]))


