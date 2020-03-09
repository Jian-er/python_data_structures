'''
    [1,3,5,7,9]
'''
# def listSum(numList):
#     sum = 0
#     for i in numList:
#         sum = sum + i
    
#     return sum 

# print(listSum([1,3,5,7,9]))

'''
    listSum2([1,3,5,7,9]) 
  = 1 + listSum2([3,5,7,9])
  = 3 + listSum2([5,7,9])
  = 5 + listSum2([7,9])
  = 7 + listSum2([9])
'''
# def listSum2(numList):  # 递归函数：调用自身的函数
#     if len(numList) == 1:
#         return numList[0]
#     else:
#         return numList[0] + listSum2(numList[1:])  

# print(listSum2([1,3,5,7,9]))



def toStr(n,base):
    str1 = '0123456789ABCDEF'
    # 比如0，1 < 2 
    if n < base:
        return str1[n]
    else:
        return toStr(n//base,base) + str1[n%base]


print(toStr(1453,16))

'''
   toStr(10,10) + '0'
   toStr(1,10) + '0'
   '1'
'''

# 栈  实现递归
from pythonds.basic.stack import Stack

rStack = Stack()


def toStr(n, base):
    convertString = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])

        n = n // base

    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res


print(toStr(1453, 16))

''' [0]
    100   0
    10    0
'''