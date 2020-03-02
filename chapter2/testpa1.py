# 常量与变量

import numpy as np

x = 5

# type函数用来判断变量的类型
print(type(x))

a = np.array((1,2,3,4,4))
print(a,type(a))

# 函数isinstance用来判断是否为指定类型
print(isinstance(x,int))

# python变量并不直接存储值，而是直接存储了值的内存地址或者引用，这也是变量类型随时可以改变的原因
x = 'Hello World'
print(x,type(x))

# **符号是幂乘符号
print(9**9)

# 在python中不用担心数值大小的问题，python支持任意大的数字
# python内置支持复数类型和运算
x = 3+4j
y = 5+6j
print(x+y)
# 使用abs函数可以计算复数的模
print(abs(x))
# imag虚部，real实部
print(x.imag,x.real)

x = '''Tom said,"Let's go"'''
print(x)
x = 'good '
x = x + 'morning'
print(x,x*3)
