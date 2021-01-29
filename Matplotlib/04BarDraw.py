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
x = np.arange(1, 4)
y = values[0, 3:6]
plt.bar(x, y, width=0.5, color=['red'])

plt.show()
