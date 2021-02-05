import pandas as pd
#  主键合并 mysql中数据库中外键连接
# 根据键值进行数据合并

# 加载数据
# df1 = pd.read_excel('./merge主键拼接数据.xlsx', index_col=0, sheet_name=0)
# df2 = pd.read_excel('./merge主键拼接数据.xlsx', index_col=0, sheet_name=1)

# 进行主键链接，
# 存在相同名称，且值大部分相同的列，为键

# right 右边的df
# left 左边的df

# how  链接方式
#   inner 内连接 交集        拿键所在列两个df共有的值进行链接
#   outer 外连接 并集        拿键所在列的所有值进行合并，没有的用NaN补齐
#   left 左外连接            拿左边键中的所有值，用右边的进行配合，若无则以NaN补齐
#   right 右外连接          拿右边键中的所有值，用左边的进行配合，若无则以NaN补齐

# res = pd.merge(left=df1, right=df2, how='inner', on='key')
# print('res:\n', res)

#
#    A   B  key   C   D
# 0  A1  B1  k1  C1  D1
# 1  A2  B2  k2  C2  D2
# 2  A3  B3  k3  C3  D3
# res = pd.merge(left=df1, right=df2, how='outer', on='key')
# print('res:\n', res)
#       A    B key    C    D
# 0   A1   B1  k1   C1   D1
# 1   A2   B2  k2   C2   D2
# 2   A3   B3  k3   C3   D3
# 3   A4   B4  kx  NaN  NaN
# 4  NaN  NaN  ky   C4   D4

# res = pd.merge(left=df1, right=df2, how='left', on='key')
# print('res:\n', res)

#      A   B key    C    D
# 0  A1  B1  k1   C1   D1
# 1  A2  B2  k2   C2   D2
# 2  A3  B3  k3   C3   D3
# 3  A4  B4  kx  NaN  NaN
# res = pd.merge(left=df1, right=df2, how='right', on='key')
# print('res:\n', res)
# res:
#       A    B key   C   D
# 0   A1   B1  k1  C1  D1
# 1   A2   B2  k2  C2  D2
# 2   A3   B3  k3  C3  D3
# 3  NaN  NaN  ky  C4  D4
# 只有列方向，没有行方向
# suffixes 如果俩表中存在列名相同的列，那么可以指定其后缀
# 主键列名称不同，但其值大部分相同  此时可以使用left_on 和 right_on  可以拿共同拥有的键值进行拼接
df1 = pd.read_excel('./merge主键拼接数据.xlsx', index_col=0, sheet_name=2)
df2 = pd.read_excel('./merge主键拼接数据.xlsx', index_col=0, sheet_name=3)
print('df1:\n', df1)
print('df2:\n', df2)

# df1:
#      A   B  Kx
# 1  A1  B1  k1
# 2  A2  B2  k2
# 3  A3  B3  k3
# 4  A4  B4  kx
# df2:
#      C   D  Ky
# 1  C1  D1  k1
# 2  C2  D2  k2
# 3  C3  D3  k3
# 4  C4  D4  ky

res = pd.merge(left=df1, right=df2, left_on='Kx', right_on='Ky', how='right')
print('res:\n', res)

# res:
#       A    B   Kx   C   D  Ky
# 0   A1   B1   k1  C1  D1  k1
# 1   A2   B2   k2  C2  D2  k2
# 2   A3   B3   k3  C3  D3  k3
# 3  NaN  NaN  NaN  C4  D4  ky
