# 删除行列
import pandas as pd

# 加载数据
users = pd.read_excel('./users.xlsx')
print('users:\n', users)
print('列索引:\n', users.columns)

# DROP
# labels 删除指定的行名称 列名称
# axis  0行 1列
# 0时label为行
# inplace 是否对原df阐述影响
# True删除原来的df
# 会返回一个删除后的结果 res =

# 列

# users.drop(labels=['sex', 'poo', 'age'], axis=1, inplace=True)
# print('删除之后的结果:\n', users)


# 行

users.drop(labels=[0, 1, 2, 3, 4, 5, 6, 12, 10], axis=0, inplace=True)
print('删除之后的结果:\n', users, users.shape)

# 删除满足条件的

# 删除男的
# bool_mask = users['sex'] == '男'
# labels = users.loc[bool_mask, :].index
# users.drop(labels=labels, axis=0, inplace=True)
# print('删除后的结果:\n', users)


# 保存不满足条件的数据
bool_mask = users['sex'] != '男'
labels = users.loc[bool_mask, :].index
users.drop(labels=labels, axis=0, inplace=True)
print('删除后的结果:\n', users)
