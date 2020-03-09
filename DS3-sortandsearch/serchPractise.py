
# def serch(alist, item):
#     found = False
#     for i in alist:
#         if item == i:
#             found = True
#     return found
#
# alist = [1,4,35,60,90]
# print(serch(alist, 90))


# def orderedSequentialSearch(alist, item):
#     pos = 0
#     found = False
#     stop = False
#
#     while pos<len(alist) and not found and not stop:
#         if alist[pos] == item:
#             found = True
#         else:
#             if alist[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#
#     return found
#
# testList = [13,20,49,50,58,63,70,100]
# print(orderedSequentialSearch(testList, 53))


# def binarySearch(alist, item):
#     found = False
#     first = 0
#     last = len(alist) - 1
#
#     while first<= last and not found:
#         midpoint = (first+last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint - 1
#
#     return found
#
# testList = [1,3,4,7,8,15,18,20,25,32]
# print(binarySearch(testList, 3))

def binarySearch(alist, item):
    if len(alist) == 0:
        return False

    midpoint = len(alist)//2
    if alist[midpoint] == item:
        return True
    else:
        if alist[midpoint] >item:
            return binarySearch(alist[:midpoint], item)
        else:
            return binarySearch(alist[midpoint+1:], item)

testList = [1,3,4,7,8,15,18,20,25,32]
print(binarySearch(testList, 3))