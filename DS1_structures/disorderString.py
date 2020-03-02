"""
乱序字符串是指一个字符串只是另一个字符串的重新排列
比如:pythonn typhon  head deah
目的：
    写一个布尔函数（返回值是布尔值的函数）
    solutions1('abcd','dbca')
"""

# 穷举法：排除  原因：如果字符串过长，20个长度

# 检查 第一个字符串是不是出现在第二个字符串中  O(n)
def solutions1(str_one, str_two):
    if len(str_one) != len(str_two):
        return False
    for s in str_one:
        if s not in str_two:
            return False
    return True

# 计数比较法  aaaabbbbcccc  ccccaaaadddd
# 计算每个字符出现的次数  26 = [a, b, c ...]

def solutions2(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26  # 初始化0列表，长度26

    for i in s1:
        pos = ord(i) - ord('a')  # 返回ASCII码，用于计算字符在列表中对应的位置
        c1[pos] += 1

    for i in s2:
        pos = ord(i) - ord('a')
        c2[pos] += 1

    j = 0
    flag = True

    while j < 26 and flag:
        if c1[j] == c2[j]:
            j += 1
        else:
            flag = False

    return flag

# 排序和比较

def solutions3(s1,s2):
    alist = list(s1)  # 转化为可变对象
    blist = list(s2)

    alist.sort()  # 列表排序
    blist.sort()

    flag = True
    i = 0

    while i < len(alist) and flag:
        if alist[i] == blist[i]:
            i += 1
        else:
            flag = False

    return flag

