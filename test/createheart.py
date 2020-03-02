# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math


# 设置X,Y轴的数值
# 一种心形线的表达方式
# x = 16*(sin(t))**3
# y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)

t=np.linspace(0,2*math.pi,3000)
x=16*(np.sin(t))**3
y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

# 创建绘图对象
plt.figure(figsize=(8,8))

# 在当前绘图对象进行绘图（两个参数是x,y轴的数据）
plt.plot(x,y,color="red",linewidth=2)

# 关闭坐标轴（也没有四边外框，仅有图像）
plt.axis('off')

# 关闭坐标刻度（但还有四条边框）
#plt.xticks([])
#plt.yticks([])

# 填充红色
plt.fill(x,y,'red')

# 提示：要先保存，再显示。顺序反了，会只得到一张空白图片
# 保存图片
# .png文件能实现背景透明
#plt.savefig("plot.png",dpi=300,bbox_inches='tight', transparent=True)
plt.savefig("plot.png",dpi=300)


# 显示图
plt.show()