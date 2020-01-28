def find(grid, num)->bool:
	row = len(grid)
	column = len(grid[0])

	i = 0
	j = column-1
	while i<row and j>=0:
		if grid[i][j]==num:
			return True
		elif grid[i][j]<num:
			i += 1
		else:
			j -= 1	
	return False

grid = [[1, 2, 8, 9],
       [2, 4, 9, 12],
       [4, 7, 10, 13],
       [6, 8, 11, 15]]

number = 7

if __name__ == '__main__':
	print(find(grid,number))