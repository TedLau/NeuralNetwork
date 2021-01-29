import matplotlib.pyplot as plt
import numpy as np

# 绘图三部曲
# 1.创建画布
# figure args: figsize 大小 dpi 像素 返回值 画布对象
# 2.绘制图形
plt.figure()
# 默认不支持中文  使其支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 支持负号
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 8)
y = np.array([11, 11, 14, 15, 16, 13, 12])
plt.plot(x, y)
plt.title('NBNBAWeek')
plt.xlabel('日期')
plt.ylabel('温度')
# 讲横轴的序号替换为中文 --修改横轴刻度
# Note:将序号替换为中文 --
# 参数一:需要被替换的序号
# 参数二:替换后的中文
# 构建中文日期列表
xticks = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
plt.xticks(x, xticks)  # rotation 度数
# 增加图例
plt.legend(['北京'])
# 修改纵轴刻度
# Note:只需要将新的刻度范围传进去。
yticks = np.arange(-15, 31, 3)
plt.yticks(yticks)

# 横纵坐标标注
for i, j in zip(x, y):  # +0.5是为了控制高度
    plt.text(i, j + 0.5, '%d°C' % j)
# 保存图片
# plt.savefig('./name.png')
plt.show()
# 图形展示
