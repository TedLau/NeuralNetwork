# 横向堆叠 -  在列方向上进行拼接合并 X轴方向  水平方向
import pandas as pd

# 加载数据
df1 = pd.read_excel('./concat直接拼接数据.xlsx', sheet_name=0, header=1)
df2 = pd.read_excel('./concat直接拼接数据.xlsx', sheet_name=1 , header=1)
print('df1:\n', df1)
print('df2:\n', df2)

# axis = 1 在列方向上
# outer 外连接 求并集
# 在横向 直接堆叠 在行的方向求所有行的并集，如果没有出现，则用NaN补齐
# inner 在横向直接堆叠 在行方向是哪个求所有行的交集

# 在横向，直接堆叠，在行的方向，求所有行的交集
res = pd.concat((df1, df2), axis=1, join='inner')
print('res列:\n', res)

res = pd.concat((df1, df2), axis=0)
print('res行:\n', res)

# 有问题，横竖一样
