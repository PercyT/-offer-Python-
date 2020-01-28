def findSum(n):
    """递归方程式f[i][j] = f[i-1][j-1]+f[i-1][j-2]
    +f[i-1][j-3]+f[i-1][j-4]+f[i-1][j-5]+f[i-1][j-6]"""
    if n<0:
        return
    arr = [[0 for i in range(6*n + 1)] for i in range(n+1)]
    for i in range(6):
        arr[1][i+1] = 1
    for i in range(2,n+1):
        for j in range(i,6*i+1):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j-2]+arr[i-1][j-3]+arr[i-1][j-4]+arr[i-1][j-5]+arr[i-1][j-6]
            
