# 一些实用的函数

import random

# 映射函数map
print(list(map(str,range(5))))

def add5(v):
    return v+5

print(list(map(add5,range(10))))

def add(x,y):
    return x+y

print(list(map(add,range(5),range(5,10))))

# 使用lambda可以实现同样的功能
print(list(map(lambda x,y: x+y,range(5),range(5,10))))

x=random.randint(1,1e30)
# 提取大整数每位上的数字
print(list(map(int,str(x))))
