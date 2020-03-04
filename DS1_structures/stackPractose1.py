# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)


from pythonds.basic.stack import Stack
#
# s = Stack()
#
# print(s.isEmpty())
# s.push(1)
# s.push('aaa')
#
# print(s.peek())
#
# s.push(True)
#
# print(s.size())
#
# print(s.isEmpty())
#
# s.push(1.1)
# print(s.pop())


def parChecker(symbolString):
    s = Stack()
    flag = True
    index = 0

    while index < len(symbolString) and flag == True:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                flag = False
            else:
                s.pop()
        index += 1

    if flag and s.isEmpty():
        return True
    else:
        return False

print(parChecker("(())"))