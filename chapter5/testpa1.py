'''
@Description: 函数
@version: 1.0
@Author: xasmall
@Date: 2020-03-05 15:01:57
@LastEditors: xasmall
@LastEditTime: 2020-03-05 15:58:30
'''
'''
递归函数：
    1.每次递归应保持问题性质不变
    2.每次递归应使用更小或更简单的输入
    3.必须有一个能够直接处理而不需要再次进行递归的特殊情况来保证递归程序可以结束
    4.函数递归深度不能太大，否则会引起内存崩溃
'''
from random import randint

'''
@name: 使用递归进行因式分解
@param:{num：因式分解的数字，fac：列表，进行存储因数}
@return: 
'''
def fun1(num,fac=[]):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            fac.append(i)
            fun1(num//i,fac)
            break
    else:
        fac.append(num)

facs = []
n = randint(2,10**8)
fun1(n,facs)
result = '*'.join(map(str,facs))
if n==eval(result):
    print(n,'=',result)

'''
函数参数问题：
    1.位置参数
    2.默认参数
    3.关键参数
    4.可变长度参数
    5.传递参数时的序列解包
'''

# 2.默认值参数
def say(message,times=1):
    print((message+' ')*times)

# 3.关键参数：明确指定哪个值传递给那个参数，实参顺序可以和形参顺序不一致，但不影响参数值的传递结果
def demo1(a,b,c):
    print(a,b,c)

demo1(b=3,a=2,c=3)

# 可变长度参数
# *parameter,**parameter,前者用来接收任意多个位置实参并将其放在一个元组中，后者用来接受多个关键参数并将其放入字典中

def demo2(*p):
    print(p)

demo2(1,2,3)

# 接收关键参数
def demo3(**p):
    for item in p.items():
        print(item)
    
demo3(x=1,y=2,c=4)

# 传递参数时的序列解包：python解释器将自动进行解包，然后将序列中的值分别传递给多个形参变量
def demo4(a,b,c):
    print(a,b,c)

seq = [1,2,3]
tup = (1,2,3)
dic = {1:'a',2:'b',3:'c'}
print(*seq)
print(*tup)
print(*dic)
print(*dic.values())

# 对于字典，可以使用**进行解包，它将转换成为类似与关键参数的形式进行参数传递
p = {'a':1,'b':2,'c':3}
demo4(**p)

demo3(**p)

'''
变量作用域：在函数内如果只引用某个变量的值而没有为其赋值，该变量为(隐式的)全局变量
            在函数内有为变量赋值的情况，该变量被认定为(隐式的)局部变量，除非在函数内赋值操作之前显式地用关键字global进行了声明
'''


# yield
def f():
    a,b = 1,1
    while True:
        yield a     #暂停执行，需要时再生成一个新元素
        a,b = b,a+b
    
a = f()
for i in range(10):
    print(a.__next__(),end=' ')
print()
for i in f():
    if(i>100):
        print(i)
        break

def demo10(s):
    result1 = [0,0]
    for ch in s:
        if ch.islower():
            result1[1] += 1
        elif ch.isupper():
            result1[0] += 1
    return tuple(result1)

tup2 = demo10('HIGUfaigaiHvfaduyvdjvHBII')
print(tup2)


