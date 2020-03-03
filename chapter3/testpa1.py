# 列表
import random
import os
from random import randint

a_list = ['a','b','c','d']
print(a_list)
# 空列表
a_list=[]
print(a_list)

# list()函数可以将元组、range对象、字符串、字典、集合或其他可迭代对象转换为列表
print(list((3,4,5,6)))
print(list(range(1,10,2)))
print(list('hello world'))
print(list({1,3,5,7}))
print(list({'a':3,'b':5,'c':7}))
print(list({'a':3,'b':5,'c':7}.items()))
print(list({'a':3,'b':5,'c':7}.values()))

# 当一个列表不在使用使，使用del命令进行删除
del a_list

# 关于列表元素的访问
x = list('python')
print(x)
print(x[1],x[-3])

# 列表常用的方法

x = [1,2,3]
x.append(4)
print(x)

# 插入
x.insert(0,0)
# 追加
x.extend([5,6,7])
print(x)


# pop函数用于删除并返回指定位置上的元素(默认是最后一个)
x = [1,2,3,4,5,6,7]
print(x.pop())

print(x.pop(0))

# remove函数用于删除列表中第一个值与指定值相等的元素，如果不存在则抛出异常
x = [1,2,1,1,2]
x.remove(2)
print(x)
# del命令删除指定位置上的元素
del x[3]
print(x)

# count用于返回指定元素出现的次数
x = [1,2,2,3,3,3,4,4,4,4,4]
print(x.count(3))
# index用于返回指定元素在列表中首次出现的位置
print(x.index(4))

# sort函数按照指定规则对列表中所有元素进行原地排序
x = list(range(11))
random.shuffle(x)
print(x)

x.sort(key=lambda item: len(str(item)),reverse=True)
print(x)
x.sort(key=str)

# 列表对象支持的运算符
x = [1,2,3]
x = x+[4]
print(x)

x = [1,2,3,4]
x = x*2
print(x)

# 比较符，逐个比较对应位置的元素，直到某个元素能够比较出大小
print([1,2,4]>[1,2,3,4])

# all函数测试是否所有元素都等价与True
# any函数测试是否存在等价于True的元素

# 列表推导式
alist = [x+x for x in range(30)]
freshFruit = [' banana',' loganberry','passion fruit']
alist = [w.strip() for w in freshFruit]

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])


# '.'表示当前文件夹
x = [filename for filename in os.listdir('.')]
print(x)

a = [-1,-4,2,3,-11,-2.3,4.5]
print([i for i in a if i>0])

x = [randint(1,10) for i in range(20)]
m = max(x)
# 查找最大元素的所有位置
print([index for index,value in enumerate(x) if value==m])

print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
print([(x,y) for x in [1,2,3] if x==1 for y in [3,1,4] if y!=x])

'''
关于切片：适用于列表、元组、字符串、range对象
[start:end:step]
start表示切片开始的位置，默认是0，第二个数字end表示切片截止位置(不包含，默认为列表长度)，step表示步长(默认为1)
'''
alist = [3,4,5,6,79,11,13,15,17]
print(alist[::])
# 逆序
print(alist[::-1])
print(list(reversed(alist)))

# 使用切片添加元素
alist = [3,5,7]
alist[len(alist):]=[9]
alist[:0]=[1,2]
alist[3:3]=[4]
print(alist)

# 使用切片替换元素
alist = [3,5,7,9]
alist[:3]=[1,2,3]
print(alist)
alist[3:]=[4,5,6]
print(alist)

# 隔一个修改一个,两边列表长度保持一致
alist[::2]=['a','b','c']
print(alist)
alist[::3]=['d','e']
print(alist)

# 使用切片删除列表中的元素
alist = [3,5,7,9]
alist[:3]=[]
print(alist)

alist = [3,5,7,9,11]
del alist[::2]
print(alist)