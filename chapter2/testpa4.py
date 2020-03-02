# 类型转换与判断

from random import randint

# 将数字转换为八进制串
print(bin(555))
# 将数字转换为八进制串
print(oct(555))
# 将字符串转换为十六进制串
print(hex(555))

# float函数将其他类型转换成实数，complex用来生成复数
print(float(3))
print(float('3.5'))
# inf无穷大
print(float('inf'))
# complex用来生成复数
print(complex(3))
print(complex(3,5))
print(complex('inf'))

# ord用来返回单个字符的Unicode码,chr用来返回Unicode编码对应的字符
print(ord('a'))
print(chr(65))
print(chr(ord('A')+1))
# str将其他类型的变成字符串
print(str(1234))
print(str([1,2,3]))
print(str((1,2,3)))
print(str({1,2,3}))

# list()、tuple()、dict()、set()用来把其他类型的数据转换成列表、元组、字典和可变集合
print(list(range(5)))
print(tuple(range(5)))
print(dict(zip('1234','abcde')))
print(set('12342356'))

# eval()用来计算字符串的值
print(eval('3+5'))
print(eval(b'3+5'))
print(eval('9'))
print(int('09'))

print(eval(str([1,2,3,4])))

# type和instance用来判断数据的类型
print(type({3}) in (list,tuple,dict))

# 最值与求和
# a包含10个[1,100]之间随机数的列表
a = [randint(1,100) for i in range(10)]
print(max(a),min(a),sum(a))
# 求得平均值
print(sum(a)/len(a))

# 函数max和min还支持key参数,用来指定比较大小的依据或者规则
print(max(['2','111'],key=len))

lst = [[randint(1,50) for i in range(5)] for j in range(30)]

print(max(lst,key=sum))
print(max(lst,key=lambda x: x[1]))

