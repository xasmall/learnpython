'''
@Descripttion: 元组的操作内容
@version: 1.0
@Author: xasmall
@Date: 2020-03-03 14:10:35
@LastEditors: xasmall
@LastEditTime: 2020-03-03 16:18:38
'''

# 元组被称为常量列表，或者“轻量级列表
# 元组属于不可变序列，不可以直接修改元组中元素的值，也无法为元组增加或删除元素
x = (1,2,3)
# 如果只有一个元素，必须在后面多谢一个逗号
x = (3,)
print(x)

# 生成器表达式
'''
使用生成器生成对象时，需要根据需要将其转换为列表和元组，也可以使用生成器对象
的__next__方法或者内置函数next进行遍历，或者直接使用for循环来遍历其中的元素
但是不管用那种方法访问其元素，只能从前往后正向访问其中的元素。当所有元素访问
结束以后，如果需要重新访问其中的元素，必须重新创建该生成器的对象
'''
g = ((i+2)**2 for i in range(10))
print(tuple(g))
# 生成器对象已遍历结束
print(list(g))

g = ((i+2)**2 for i in range(10))
# 使用__next__方法获取元素
print(g.__next__())
print(g.__next__())
print(next(g))

g = ((i+2)**2 for i in range(10))
for item in g:
    print(item,end=' ')

print()

g = map(str,20)
print('2' in g)
print('2' in g)