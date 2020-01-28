import time
import copy
class Solution:
    def InversePairs(self, array):
        if not array:
            return 0
        arrCopy = copy.deepcopy(array)
        return self.InverseRecur(array, arrCopy, 0, len(array)-1)

    def InverseRecur(self, array, arrCopy, start, end):
        if start == end:
            return 0
        mid = (start + end) // 2
        left = self.InverseRecur(array, arrCopy, start, mid)
        right = self.InverseRecur(array, arrCopy, mid+1, end)
        count = 0
        i = mid
        j = end
        locCopy = end
        while i>=start and j > mid:
            if array[i] > array[j]:
                count += j - mid
                arrCopy[locCopy] = array[i]
                locCopy -= 1
                i -= 1
            else:
                arrCopy[locCopy] = array[i]
                locCopy -= 1
                i -= 1

        while i >= start:
            arrCopy[locCopy] = array[i]
            locCopy -= 1
            i -= 1
        while j > mid:
            arrCopy[locCopy] = array[j]
            locCopy -= 1
            j -= 1
        s = start
        while s <= end:
            array[s] = arrCopy[s]
            s += 1
        return left + right + count

if __name__ == '__main__':
    a = [1,2,['A','B']]
    print('a={}'.format(a))
    b = a[:]
    a[0] = 9 #修改b的最外层元素，将1变成9
    a[2][0] = 'D' #修改b的内嵌层元素
    print('a={}'.format(a))
    print('b={}'.format(b))
    print('id(a)={}'.format(id(a)))
    print('id(b)={}'.format(id(b)))