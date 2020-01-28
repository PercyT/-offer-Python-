class Solution():
	def judge(self,i,j,k):
		if (sum(map(int, str(i) + str(j))))<=k:
			return True
		else:
			return False

	def movieStart(self,rows,cols,k):
		martix = [[0 for i in range(cols)] for j in range(rows)]
		count = self.movieCount(rows,cols,martix,0,0,k)
		print(martix)
		return count

	def movieCount(self,rows,cols,martix,i,j,k):
		count = 0
		if i<rows and j<cols and i>=0 and j>=0 and self.judge(i,j,k) and martix[i][j]==0:
			martix[i][j] = 1 # 表示已经访问过
			count = 1 + self.movieCount(rows,cols,martix,i+1,j,k)\
			+ self.movieCount(rows,cols,martix,i-1,j,k)\
			+ self.movieCount(rows,cols,martix,i,j+1,k)\
			+ self.movieCount(rows,cols,martix,i,j-1,k)
		return count

s = Solution()
count = s.movieStart(3,3,2)
print(count)
