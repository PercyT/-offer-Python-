def printMatrix(num, columns, rows):
	if num is None or columns<=0 or rows<=0:
		return

	start = 0
	while(start*2<columns and start*2<rows):
		printMatrixCircle(num,columns,rows,start)
		start = start + 1

def printMatrixCircle(num, columns, rows, start):
	endY = rows-1-start
	endX = columns-1-start

	for i in range(start, endX+1):
		print(num[start][i])

	if start<endY:
		for i in range(start+1, endY+1):
			print(num[i][endY])

	if start<endY and start<endX:
		for i in range(endY-1, start-1, -1):
			print(num[endX][i])

	if start+1<endY and start<endX:
		for i in range(endX-1, start-1, -1):
			print(num[i][start])

if __name__ == '__main__':
	num = [[0 for i in range(3)] for i in range(3)]
	for i in range(2):
		num[i][0] = 1
	printMatrix(num, 3, 3)
