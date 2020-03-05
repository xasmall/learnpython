'''
@Description: 
@version: 
@Author: xasmall
@Date: 2020-03-02 19:19:32
@LastEditors: xasmall
@LastEditTime: 2020-03-05 12:41:01
'''
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

# reduce()可以将一个接受两个参数的函数以迭代累计的形式从左到右依次作用到一个序列或迭代器对象的所有元素

from functools import reduce
print(reduce(lambda x,y: x+y,range(1,10)))
# filter()将一个单参数函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象，如果指定函数为None，则返回序列中等价于True的元素
seq=['foo','x41','!?','***']
def fun(x):
    return x.isalnum()  #用于测试x是否为字母或数字

print(list(filter(fun,seq)))

# range()函数
print(list(range(1,10,2))) #2是步长

# zip()函数用于把多个可迭代对象中对应位置的元素压缩到一起，返回一个可迭代的zip对象
print(list(zip('abcd','123')))
print(list(zip('abcd')))
print(list(zip('abcd','123',',.!')))

# zip对象只能遍历一次，访问过的元素就不存在了
x=zip('abcd','1234')
print(list(x))
print(list(x))