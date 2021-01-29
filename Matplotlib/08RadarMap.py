import matplotlib.pyplot as plt
import numpy as np

# 从不同的方向来剖析一个对象在不同方向上的评价，可以用来绘制(高纬度)数据
# 使用平面雷达图可以描述高维度空间的点——使用列数超过2的数组来表示
# 主要采用的是 极坐标

# 创建画布
plt.figure()
# 默认不支持中文  使其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 支持负号
plt.rcParams['axes.unicode_minus'] = False
# 绘图

# 绘制雷达图
datalength = 5
angle = np.linspace(0, 2 * np.pi, datalength, endpoint=False)

print(angle)
# 角度闭合
angle = np.concatenate((angle, [angle[0]]), axis=0)

data = np.array([2, 3.5, 4, 4.5, 5])
# 数据闭合
data = np.concatenate((data, [data[0]]), axis=0)
print(data)
plt.polar(angle, data, color='r', marker='*', markersize=15)

# 构建刻度
xticks = ['生存评分', '输出评分', '团战评分', 'KDA', '发育评分']
xticks = np.concatenate((xticks, [xticks[0]]), axis=0)
plt.xticks(angle, xticks)
# 图形展示
plt.show()
