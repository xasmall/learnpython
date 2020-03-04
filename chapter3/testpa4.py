'''
@Descripttion: 集合操作
@version: 1.0
@Author: xasmall
@Date: 2020-03-03 16:56:11
@LastEditors: xasmall
@LastEditTime: 2020-03-04 10:48:40
'''
import random
from random import randrange

a = {3,5}

# 将range对象转换为集合
a_set = set(range(8,14))
# 转换时自动去掉重复元素
b_set = set([0,1,2,3,0,1,2,3,7,8])

print(b_set)

# 集合操作和运算
# 自动忽略重复元素
s = {1,2,3}
s.add(3)
print(s)
s.update({3,4})
print(s)

'''
删除元素操作
    remove方法用于删除集合中的元素，如果指定元素不存在则抛出异常
    pop方法用于随机删除并返回集合中的一个元素
    discard方法用于删除一个特定元素，如果元素不在集合中则忽略该操作
'''

s.discard(5)
print(s)
print(s.pop())

'''
集合中的一些操作：
    并集：|
    交集：&
    差集：-
    对称差集：^
    子集：<=,>=
    真子集：<,>
'''

a = {8,9,10,11,12,13}
b = {0,1,2,3,7,9}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

# 生成100个1000以内的列表
listrandom = [random.choice(range(1000)) for i in range(100)]
print(set(listrandom))
newset = set(listrandom)
print(len(newset))

'''
@name: 添加指定范围的指定数目的不重复数字
@msg: 
@param {number,start,end} 
@return: 不重复数字的集合
'''
def randomNumber(number,start,end):
    data = set()
    while(len(data)<number):
        element = random.randint(start,end)
        data.add(element)
    return data

data = randomNumber(10,1,100)
print(data)

'''
集合操作实例：电影评分与推荐
'''
# 模拟用户打分数据，为5部电影打分
data = {'user'+str(i):{'film'+str(randrange(1,15)):randrange(1,6) for j in range(randrange(3,10))} for i in range(10)}
# 模拟当前用户打分数据
user = {'film'+str(randrange(1,15)):randrange(1,6) for i in range(5)}

f = lambda item:(-len(item[1].keys()&user),sum(((item[1].get(film)-user.get(film))**2 for film in user.keys()&item[1].keys())))

similarUser,films = min(data.items(),key=f)

print('known data'.center(50,'='))
for item in data.items():
    print(len(item[1].keys()&user.keys()),sum(((item[1].get(film)-user.get(film))**2 for film in user.keys()&item[1].keys())),item,sep=':')

print('current user'.center(50,'='))
print(user)
print('most similar user and his film'.center(50,'='))
print(similarUser,films,sep=':')
print('recommended film'.center(50,'='))
# 集合的差集
print(max(films.keys()-user.keys(),key=lambda film: films[film],default='not exists'))

# 序列解包
x,y,z = 1,2,3
print(x,y,z)
v_tuple =(False,3.5,'exp')
print(x,y,z)
x,y,z = v_tuple
x,y = y,x
print(x,y,z)
x,y,z = range(3)
x,y,z = map(str,range(3))
print(x,y,z)
'''
序列解包可以用于列表、字典、enumerate对象、filter对象、zip对象，默认对字典的键进行操作
字符串也支持序列解包
'''
keys = ['a','b','c']
values = [1,2,3,4]
for k,v in zip(keys,values):
    print(k,v)
