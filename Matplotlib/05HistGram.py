import matplotlib.pyplot as plt
import numpy as np

height = np.random.uniform(low=140, high=190, size=30)
print(height)
group_num = 30
height = np.array([float('%.1f' % i) for i in height])
print(height)

# 传入真实的数据，再传入如何分组 那么默认将所有的数据以直方图的形式展示出来
# 传入数据
# 具体分组 多少个组
plt.figure()
# plt.hist(height, bins=10)

# 自定义分组  指定分组节点
bins = [140, 150, 160, 170, 180, 190]
# 自定义等宽分组
# 1、确定分组组数，2、确定步长（最大值，最小值、间距）3、确定分组节点
max_h = np.max(height, axis=0)
min_h = np.min(height, axis=0)
# 向上取整  转为整型数据
width = np.ceil((max_h - min_h) / 5)
# +width是为了能包含最大值
bins = np.arange(min_h, max_h + width, width)

# 修改刻度
plt.xticks(bins)
plt.hist(height, bins=bins, color='#ADD8E6', edgecolor='k')
# 添加网格线 plt.grid(b=True,axis='y)

plt.show()


# 与柱状图的区别
# 直方图展示的是数据的分布 柱状图比较的是数据的大小
# 直方图X为定量数据，柱状图X为分类数据
# 直方图柱子间一般无间隔

# 注意点：
# 组距 --组数
