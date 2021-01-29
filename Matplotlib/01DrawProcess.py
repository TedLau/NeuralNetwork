import matplotlib.pyplot as plt
import numpy as np

# 绘图三部曲
# 1.创建画布
# figure args: figsize 大小 dpi 像素 返回值 画布对象
# 2.绘制图形
plt.figure()

x = np.arange(1, 8)
y = np.array([11, 11, 14, 15, 16, 13, 12])
plt.plot(x, y)
plt.show()
# 图形展示
