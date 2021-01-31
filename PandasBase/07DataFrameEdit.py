#  已存在数据进行重新赋值

import pandas as pd

# 加载数据

users = pd.read_excel('./users.xlsx')
print('users:\n', users)
print('users 列索引:\n', users.columns)

# 满足条件的才进行修改

# 1、循环遍历 if 条件判断
# 2、bool数组索引操作
# a、找到符合的数据
bool_mask = users['age'] % 2 == 0
print('bool_mask:\n', bool_mask)
# 修改
users.loc[bool_mask, 'age'] = 100
print('满足条件的结果:\n', users[['NAME', 'age']])
