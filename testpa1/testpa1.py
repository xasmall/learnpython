# 每个import语句只导入一个模块，最好按照标准库、扩展库、自定义库的顺序依次导入
import math as m
import random as random
import os.path as path
# 导入扩展库
import numpy as np
# 导入自定义库

import hello

# 计算最大公约数
print(m.gcd(56,64))

# 获得[0,1)内的随机小数
n1 = random.random()

# 获得[0,100]内的随机整数
n2 = random.randint(1,100)

# 获得[0,100)内的随机整数
n3=random.randrange(1,100)
print(n1,n2,n3)

# 判断是否是文件
print(path.isfile(r'E:\gitresposity\learnpython\readme.txt'))

a=np.array((1,2,3,4,5))
print(a)

hello.main()