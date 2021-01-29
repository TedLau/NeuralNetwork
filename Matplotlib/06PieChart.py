import matplotlib.pyplot as plt
import numpy as np

# 可以用来对比部分与整体的关系也可以用来比较部分与部分的关系
# plt.pie

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

print('values', values)
# 创建画布
plt.figure()
# 绘制图形
# 图形展示
x = values[-1, 3:6]
# labels 各部分的名称
labels = [i[:4] for i in columns[3:6]]
# 　增加阴影 shadow
#   explode 离心半径 各部分扇形距离饼心的距离
explode = (0.01, 0.02, 0.03)
# colors 饼图的颜色
# autopct ---各部分占比的情况
autopct = '%.2f%'
# pctdistance  表示占比情况距离饼心的距离 默认为0.6半径
# labeldistance 表示labels距离饼心的距离 默认1.1半径
# radius 饼图的半径
plt.pie(x, labels=labels, shadow=True, explode=explode)
plt.axis('equal')
# 增加图例
plt.legend(labels)

# plt.shadow
# 增加标题
plt.title('2017年第一季度各个产业的增加总值占比饼图')
plt.show()
