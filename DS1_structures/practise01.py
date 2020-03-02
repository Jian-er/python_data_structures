"""
问题描述：求前n个整数的和
"""
import time

def sumOfN(n):
    start_time = time.time()
    sum = 0
    for i in range(1, n+1):
        sum += i
    end_time = time.time()
    return sum, end_time-start_time

print("计算的结果是%d 需要%10.7f秒"%sumOfN(10000))


# 高斯函数
def sumOfN2(n):
    return (n*(n+1))/2

start_time = time.time()
print(sumOfN2(10000))
end_time = time.time()
print(end_time-start_time)
