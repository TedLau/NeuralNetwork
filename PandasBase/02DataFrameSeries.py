import pandas as pd

df = pd.DataFrame(
    data={
        'name': ['zs', 'ls'],
        'age': [21, 22],
        'group': [12, 122]

    },
    index=['s1', 's2']
)
print(df)
# df中的数据元素
# 可以通过df.values 将其转为ndarray
# 也可以将ndarray使用pd.DataFrame 转为 df

# 属性
# dataframe属性
# values index columns size ndim shape
# print('df values:\n',df.values)
# # [['zs' 21 12]
# #  ['ls' 22 122]]
# print('type:\n',type(df.values))
# # <class 'numpy.ndarray'>
# print('*'*100)
# print('df index:\n',df.index)  # 行索引
# # Index(['s1', 's2'], dtype='object')
# print('columns:\n',df.columns) # 列索引
# # Index(['name', 'age', 'group'], dtype='object')
# print('size:\n',df.size)
# # 6
# print('df ndim:\n',df.ndim)
# # 2
# print('df shape:\n',df.shape)
# # (2, 3)
# print('df dtype:\n',df.dtypes)
# #  name     object
# # age       int64
# # group     int64
# # dtype: object


# series属性  无colums属性 有dtype 属性
# 元素 可以通过 pd.series 转为ndarray
se = df['age']
print('se:\n', se)
#  s1    21
# s2    22
# Name: age, dtype: int64
print('se type:\n', type(se))
# <class 'pandas.core.series.Series'>