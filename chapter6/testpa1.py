'''
@Description: python面向对象设计
@version: 1.0
@Author: xasmall
@Date: 2020-03-05 16:01:24
@LastEditors: xasmall
@LastEditTime: 2020-03-06 21:51:47
'''

# 私有成员和共有成员
class Test:
    # 构造方法，创建对象的时候自动调用
    def __init__(self,value=0):
        # 私有数据成员
        self.__value = value
    def setValue(self,value):
        # 在类内部可以直接访问私有成员
        self.__value = value
    def show(self):
        print(self.__value)
    
t = Test(8)
t.show()

# 特殊的形式在外部访问私有数据
print(t._Test__value)

'''
1.以一个下划线开头，保护成员，一般建议在类对象和子类对象访问这些成员，在模块中使用一个或多个下划线开头的成员不能用'from moudle import *'导入，除非在模块中使用__all__变量明确这样的成员可以使用
2.以两个下划线开头但不以两个下划线结束，表示私有成员，一般只有类自已能访问，子类对象也不能访问，但在对象外部可以通过"对象名._类名__xxx"这样的特殊形式进行访问
3.前后个两个下划线，系统定义的特殊成员
'''

# 数据成员

# 单例
class SingleInstance:
    num = 0
    def __init__(self):
        if SingleInstance.num>0:
            raise Exception('only create one object.')
        SingleInstance.num += 1

t1 = SingleInstance()
# t2 = SingleInstance()

# 成员方法

class Root:
    __total = 0
    def __init__(self,v):
        self.__value = v
        Root.__total += 1
    def show(self):
        print('self.__value:',self.__value)
        print('Root.__total:',Root.__total)
    
    @classmethod
    def classShowTotal(cls):
        print(cls.__total)

    @staticmethod
    def staticShowTotal():
        print(Root.__total)
    
r = Root(3)
r.classShowTotal()
r.staticShowTotal()

rr = Root(5)
Root.staticShowTotal()
Root.classShowTotal()

Root.show(rr)
class Test1:
    def __init__(self,value):
        self.__value = value
    
    def __get(self):
        return self.__value
    def __set(self,v):
        self.__value = v
    
    value = property(__get,__set)

    def show(self):
        print(self.__value)

class Test2:
    def __init__(self,value):
        self.__value = value
    
    def __get(self):
        return self.__value
    
    def __set(self,v):
        self.__value = v
    
    def __del(self):
        del self.__value
    
    value = property(__get,__set,__del)
    
    def show(self):
        print(self.__value)