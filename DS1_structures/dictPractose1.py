from timeit import Timer

def test1():
    dict1 = {"a":1,
             "b":2}
    dict2 = dict1.copy()

def test2():
    dict1 = {"a":1,
             "b":2}
    a = dict1.get('a')

def test3():
    dict1 = {"a":1,
             "b":2}

    dict1['a'] = 3

def test4():
    dict1 = {"a":1,
             "b":2}

    del dict1['a']


t1 = Timer('test1()','from __main__ import test1')
print('copy',t1.timeit(number=1000),'毫秒')
t2 = Timer('test2()','from __main__ import test2')
print('get',t2.timeit(number=1000),'毫秒')
t3 = Timer("test3()", "from __main__ import test3")
print("set",t3.timeit(number=1000), "毫秒")
t4 = Timer("test4()", "from __main__ import test4")
print("delete",t4.timeit(number=1000), "毫秒")