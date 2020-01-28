def getIndex(input, left, right):
	p = input[left]
	while left<right:
		while input[right]>p and left<right:
			right -= 1
		input[left] = input[right]
		while input[left]<p and left<right:
			left += 1
		input[right] = input[left]
	input[left] = p
	return left

def getLeastNumber(input, k):
	start = 0
	end = len(input)-1
	mid = getIndex(input, start, end)

	while k-1 != mid:
		if k-1 > mid:
			start = mid + 1
			mid = getIndex(input, start, end)
		else:
			end = mid - 1
			mid = getIndex(input, start, end)
	return input[:mid+1]