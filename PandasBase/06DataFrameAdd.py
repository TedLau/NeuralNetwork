# 增加操作  已有数据增加新的属性
import pandas as pd

# 加载数据
users = pd.read_excel('./users.xlsx')
print('users:\n', users)
print('列索引:\n', users.columns)

# 增加一列 下一年的年龄 next_year_age

users['next_year_age'] = users['age'] + 1
print("users:\n", users[['age', 'next_year_age']])
