def maxAfterCutting(length:int)->int:
    if length<2:
        return 0
    if length==2:
        return 1
    if length==3:
        return 2
    product = [0]*(length+1)
    print(product)
    product[0]=0
    product[1]=1
    product[2]=2
    product[3]=3
    for i in range(4,length+1):
        max = 0
        for j in range(1,i//2+1):
            new = product[i-j]*product[j]
            if max<new:
                max = new
        product[i] = max
    return product[length]

print(maxAfterCutting(8))
