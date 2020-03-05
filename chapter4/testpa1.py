'''
@Descriptions: 选择结构
@version: 1.0
@Author: xasmall
@Date: 2020-03-04 10:53:18
@LastEditors: xasmall
@LastEditTime: 2020-03-05 12:36:11
'''
# 单分支选择结构

# x = input('input two numbers:')
# a,b = map(int,x.split())
# if a>b:
#     a,b = b,a

# print(a,b)

# jitu,tui = map(int,input('请输入鸡兔总数和腿总数：').split())
# tu = (tui-2*jitu)/2
# if int(tu)==tu:
#     print('鸡: {0},兔: {1}'.format(int(jitu-tu),int(tu)))
# else:
#     print('数据不正确，无解')


# a = 5
# print(6 if a>3 else 5)


from random import randint
n = int(input('请输入一个正整数：'))
while n>1:
    print("该你拿了，现在剩余物品数量为：{0}".format(n))
    while True:
        try:
            num = int(input('请输入你要拿走的物品数量：'))
            assert 1<=num<=n//2
            break
        except:
            print('最少必须拿走1个，最多可以拿走{0}个。'.format(n//2))
        
    n -= num
    if n==1:
        print('恭喜，你赢了')
        break
    n -=randint(1,n//2)
else:
    print('你输了')
