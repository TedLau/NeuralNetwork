# 重叠合并，也就是说，使用另外一个表的元素，来填充本表的对应位置上 空缺 的元素

import pandas as pd

# 加载数据

df1 = pd.read_excel('./重叠合并数据.xlsx', index_col=0, sheet_name=0)
df2 = pd.read_excel('./重叠合并数据.xlsx', index_col=0, sheet_name=1)
print('df1:\n', df1)

print('df2:\n', df2)
# df1:
#      A  B    C
# 0 NaN  3  4.0
# 1 NaN  5  NaN
# 2 NaN  7  NaN
# df2:
#     A    B  C
# 1  1  NaN  3
# 2  4  5.0  6

res = df1.combine_first(df2)
print('res:\n', res)

# res:
#       A    B    C
# 0  NaN  3.0  4.0
# 1  1.0  5.0  3.0
# 2  4.0  7.0  6.0
