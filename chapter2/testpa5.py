# 基本输入输出

import random

x = input('Please input:')
print(x)

# print函数 seq参数用于指定数据之间的分隔符，end参数用于指定输出之后的分隔符
print(1,2,3,4,sep='\t')
for i in range(10):
    print(i,end=' ')

# 排序和逆序
x=list(range(11))
random.shuffle(x)

print(x)
print(sorted(x))

print(sorted(x,key=str))
print(sorted(x,key=lambda item: len(str(item)),reverse=True))

x = ['aaaa','bc','d','b','ba']
# 先按长度排序，长度一样的正常排序
print(sorted(x,key=lambda item:(len(item),item)))
print(list(reversed(x)))

# 枚举和迭代

print(list(enumerate('abcd')))
print(list(enumerate(['Python','Greate'])))

for index,value in enumerate(range(10,15)):
    print((index,value),end='\t')