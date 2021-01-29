import matplotlib.pyplot as plt
import numpy as np

# 默认不支持中文  使其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 支持负号
plt.rcParams['axes.unicode_minus'] = False
res = np.load('./gdp.npz', allow_pickle=True)
print(res)

for i in res:
    print(i)

columns = res['columns']
values = res['values']
print(columns)
print(values)

fig = plt.figure(figsize=(16, 12), dpi=100)
# 添加子图  绘制行数和列数子图的序号
fig.add_subplot(2, 1, 1)  # 绘制两行一列的第一个子图

y = values[:, 3:6]
# 真实的数据的横轴是时间
# 先创建序号 然后自己构建
x = np.arange(values.shape[0])
plt.plot(x, y)
# 增加标题
plt.title("2000-2017年各个产业生产总值")
plt.ylabel("生产总值(亿元)")
# 图例 从columns里截取

legend = [i[:4] for i in columns[3:6]]
plt.legend(legend)

fig.add_subplot(2, 1, 2)  # 绘制两行一列的第二个子图
legend = [i[:2] for i in columns[6:]]
plt.legend(legend)
plt.ylabel('生产总值(亿元)')
plt.xlabel('时间')
# 修改横轴刻度  每隔四个显示
plt.xticks(x[::4], values[:, 1][::4], rotation=45)
# wspace ----两子图宽之间的间距  hspace 子图高度之间的间距 子图高度之间的百分比
# 调整子图之间的间距 plt.subplots_adjust()
plt.show()

# scatter 创建散点图
# y1 y2 y3
# 点的大小s 可以传递具体的值 表示这一组所有点的大小
# 一个数组 表示这一组点的各个点的大小
# c 点的颜色 可以是具体的颜色 也可以是具体的数组表示单个点的颜色
# marker 点的样式 接收特定的字符串，表示这一组所有点的样式
# alpha  透明度 0-1 值越小 越透明
