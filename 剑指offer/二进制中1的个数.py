def number(num:int)->int:
    flag = 1
    count = 0
    for i in range(0,32):
        if num&flag:
            count += 1
        flag = flag << 1
    return count

def newnumber(num:int)->int:
    """和本身先减一的数取反，然后再与"""
    count = 0 
    while num:
        count = count+1
        num = (num-1)&num
    return count
print(newnumber(10))