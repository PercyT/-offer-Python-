def longestStr(string):
 	position = [-1 for i in range(26)] # 这个数组用来存放该字母最近一次出现是在哪里，从而进行比较，-1表示没出现过
 	maxlength = 0
 	currentlength = 0
 	for i in range(len(string)):
 		if position[ord(string[i])-ord('a')]==-1 or (i-position[ord(string[i])-ord('a')])>currentlength:
 			currentlength = currentlength+1
 		else:
 			if currentlength>maxlength:
 				maxlength = currentlength
 			currentlength = i-position[ord(string[i])-ord('a')]
 		position[ord(string[i])-ord('a')] = i

 	if currentlength>maxlength:
 		maxlength = currentlength
 	return maxlength

if __name__ == '__main__':
 	print(longestStr('awdawdz'))


