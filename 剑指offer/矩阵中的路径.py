def hasPath(matrix:list,rows:int,cols:int, path:list)->bool:
	for i in range(rows):
		for j in range(cols):
			if matrix[i*cols+j]==path[0]:
				# 表示上面返回True时，匹配成功。但是返回False时并不一定匹配失败
                # 只是说明当前第一个和path[0]相同的位置匹配失败，后面可能还有匹配成功的位置！！！
                # 故不能添加 else：return False
				if findPath(matrix,rows,cols,path[1:],i,j):
					return True

def findPath(matrix,rows,cols,path,i,j):
	if not path:
		return True
	matrix[i*cols+j] = ''
	  # 然后接着找剩余字符串的第一个字符是否能和上一个匹配成功的位置的上下左右的字符匹配成功
	if j+1<cols and matrix[i*cols+j+1]==path[0]:
		return findPath(matrix,rows,cols,path[1:],i,j+1)
	elif j-1<0 and matrix[i*cols+j-1]==path[0]:
		return findPath(matrix,rows,cols,path[1:],i,j-1)
	elif i+1<rows and matrix[(i+1)*cols+j]==path[0]:
		return findPath(matrix,rows,cols,path[1:],i+1,j)
	elif i-1<0 and matrix[(i-1)*cols+j]==path[0]:
		return findPath(matrix,rows,cols,path[1:],i-1,j)
	else:
		return False

