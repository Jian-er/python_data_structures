'''
[54,26,93,17,77,31,44,55,20]
第一趟54 26  [26，54,93,17,77,31,44,55,20]
第二躺未交换  [26，54,93,17,77,31,44,55,20]
第三趟93 17  [26，54,17,93,77,31,44,55,20]
第四躺 93 77  [26，54,17,77,93,31,44,55,20]
第五躺 93 31 [26，54,17,77,31,93,44,55,20]
第六趟 93 44 [26，54,17,77,31,44,93,55,20]
第七趟 93 55 [26，54,17,77,31,44,55,93,20]
第八趟 93 20 [26，54,17,77,31,44,55,20,93]

列表中又n想哪第一遍比对需要n-1次

第二遍  [26，17,54,31,44,55,20，77,93] n-2
第三遍  [17，26,31,44,20,54,55，77,93]
第四遍  [17，26,31,20,44,54,55，77,93]
第五遍  [17，26,20,31,44,54,55，77,93]
第六遍  [17，20,26,31,44,54,55，77,93]
'''

# a和b交换
# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)
# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 temp=alist[i]
#                 alist[i]=alist[i+1]
#                 alist[i+1]=temp
# alist=[54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)
# 短冒号排序
# def bubbleSort(alist):
#     flag = True
#     passnum = len(alist) - 1
#     while passnum > 0 and flag:
#         flag=False
#         for i in range(passnum):
#             if alist[i] > alist[i + 1]:
#                 flag=True
#                 temp = alist[i]
#                 alist[i] = alist[i + 1]
#                 alist[i + 1] = temp
#         passnum = passnum - 1
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubbleSort(alist)
# print(alist)
# '''
# 选择排序
# '''
# def selectionSort(alist):
#     for fill

# '''
# 插入排序
# '''
#
#
# def insertionSort(alist):
#     for i in range(1, len(alist)):
#         currentValue = alist[i]
#         pos = i
#         while pos > 0 and alist[pos - 1] > currentValue:
#             alist[pos] = alist[pos - 1]
#             pos = pos - 1
#         alist[pos]=currentValue
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# insertionSort(alist)
# print(alist)

'''
希尔排序
'''


# def shellSort(alist):
#     sublistcount=len(alist)//2
#     while sublistcount>0:
#         for startposition in range(sublistcount):
#             gapInsertionSort(alist,startposition,sublistcount)
#         print('alist:',alist)
#         sublistcount=sublistcount//2
# def gapInsertionSort(alist, start, gap):
#     for i in range(start + gap, len(alist), gap):
#         currentValue = alist[i]
#
#         pos = i
#         while pos > 0 and alist[pos - 1] > currentValue:
#             alist[pos] = alist[pos - gap]
#             pos = pos - gap
#         alist[pos] = currentValue
#     return  alist
# alist=[54,26,93,17,77,31,44,55,20]
# shellSort(alist)


"""
    归并排序
"""

# def mergeSort(alist):
#     if len(alist)>1:
#         mid = len(alist)//2
#         leftHalf = alist[:mid]
#         rightHalf = alist[mid:]
#
#         mergeSort(leftHalf)
#         mergeSort(rightHalf)
#
#         i = 0
#         j = 0
#         k = 0
#         while i< len(leftHalf) and j < len(rightHalf):
#             if leftHalf[i] < rightHalf[j]:
#                 alist[k] = leftHalf[i]
#                 i += 1
#             else:
#                 alist[k] = rightHalf[j]
#                 j += 1
#
#             k += 1
#         while i < len(leftHalf):
#             alist[k] = leftHalf[i]
#             i += 1
#             k += 1
#         while j < len(rightHalf):
#             alist[k] = rightHalf[j]
#             j += 1
#             k += 1
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# mergeSort(alist)
# print(alist)



'''
    快速排序
'''
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

# 递归调用对数列进行分区
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

# 选出基准点
def partition(alist,first,last):
    # 定义基准点
    pivotvalue = alist[first]

    leftMark = first + 1
    rightMark = last

    # 停止比对
    done = False
    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotvalue:
            leftMark = leftMark + 1

        while alist[rightMark] >= pivotvalue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark


alist =  [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
