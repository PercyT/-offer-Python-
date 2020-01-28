def getMaxValue(values, rows, columns):
	maxValue = [[0 for i in range(0, columns)] for i in range(0, rows)]
	for i in range(0, rows):
		for j in range(0, columns):
			left = 0
			up = 0
			if i>0:
				left = maxValue[i][j-1]
			if j>0:
				up = maxValue[i-1][j]
			maxValue[i][j] = max(left,up)+values[i][j]
	return maxValue[rows-1][columns-1]

