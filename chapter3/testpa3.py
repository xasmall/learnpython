'''
@Descripttion: 字典的一些操作
@version: 1.0
@Author: xasmall
@Date: 2020-03-03 16:19:40
@LastEditors: xasmall
@LastEditTime: 2020-03-03 16:54:07
'''

import string
import random

# 字典中的"键"不允许重复，"值"可以重复

# 字典的创建与删除
aDict = {'server':'db.diveintopython3.org','database':'mysql'}
print(aDict)
# 空字典
x = dict()
x = {}
keys = ['a','b','c','d']
values = [1,2,3,4]
d = dict(zip(keys,values))
print(d)

# 以关键参数的形式创建字典
d = dict(name='Dong',age=29)
print(d)
aDict = dict.fromkeys(['name','age','sex'])
print(aDict)

# 删除字典元素
del aDict

# 字典元素的访问
aDict = {'age':29,'score':[98,97],'name':'Dong','sex':'male'}
print(aDict['age'])
print(aDict['score'])

# 指定的键不存在时返回指定的默认值
print(aDict.get('address','Not exists.'))


# 查看所有元素
print(aDict.items())

# 默认遍历所有的键
for item in aDict:
    print(item)


for item in aDict.items():
    print(item)

'''
元素的添加、修改、删除
当以指定"键"为下标，为字典元素赋值时，有两种含义：
    1.若该键存在，则表示修改该键所对应的值
    2.若不存在，则表示添加一个新的键值对，也就是添加一个新元素
'''

aDict = {'age':35,'name':'Dong','sex':'male'}
aDict['age'] = 39
print(aDict)

aDict['address'] = 'Beijing'
print(aDict)

# 使用update方法可以将另一个字典键值一次性全部添加到当前字典对象，
# 如果两个字典中存在相同的键，则以另一个字典中的值为准进行更新
aDict.update({'a':97,'age':38})
print(aDict)

# ascii_letters表示英文字母大小写，digits表示10个数字字符
x = string.ascii_letters+string.digits
z = ''.join((random.choice(x) for i in range(1000)))
d = dict()
for ch in z:
    # 如果不存在在字典里则返回为0
    d[ch]=d.get(ch,0)+1

for k,y in sorted(d.items()):
    print(k,':',y)
