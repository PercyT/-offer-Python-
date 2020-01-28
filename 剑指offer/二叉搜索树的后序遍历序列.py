def verifyBST(nums):
	if not nums:
		return

	root = nums[-1]
	for i in range(0, len(nums)):
		if nums[i]>root:
			break

	for j in range(i, len(nums)):
		if nums[j]<root:
			return False

	left = True
	right = True
	if i != 0:
		left = verifyBST(nums[0:i])
	if i < len(nums)-1:
		right = verifyBST(nums[i:-1])
	return left and right

if __name__ == '__main__':
	nums = [5,7,6,9,11,10,8]
	isTrue = verifyBST(nums)
	print(isTrue)