# 纵向堆叠
import pandas as pd

# 加载数据
df1 = pd.read_excel('./concat直接拼接数据.xlsx', sheet_name=0, header=0)
df2 = pd.read_excel('./concat直接拼接数据.xlsx', sheet_name=1, header=0)
print('df1:\n', df1)
print('df2:\n', df2)
print('1')
res = pd.concat((df1, df2), axis=0, join='inner')
print(res)
print('1')
res = pd.concat((df1, df2), axis=0)
print(res)

# append 追加 追加的时候 需要保证列名一直
# 返回追加之后的结果

# 加载数据
df1 = pd.read_excel('./append直接拼接数据.xlsx', sheet_name=0)
df2 = pd.read_excel('./append直接拼接数据.xlsx', sheet_name=1)
print('df1:\n', df1)
print('df2:\n', df2)
# df1:
#     Unnamed: 0   A   B   C
# 0           1  A1  B1  C1
# 1           2  A2  B2  C2
# 2           3  A3  B3  C3
# 3           4  A4  B4  C4
# df2:
#     Unnamed: 0   A   B   C
# 0           2  A2  B2  C2
# 1           4  A4  B4  C4
# 2           6  A6  B6  C6
# 3           8  A8  B8  C8
res = df1.append(df2)
print('追加后的结果:\n', res)
#     Unnamed: 0   A   B   C
# 0           1  A1  B1  C1
# 1           2  A2  B2  C2
# 2           3  A3  B3  C3
# 3           4  A4  B4  C4
# 0           2  A2  B2  C2
# 1           4  A4  B4  C4
# 2           6  A6  B6  C6
# 3           8  A8  B8  C8
