# 分组聚合  按照一定的规则进行分组，在各组内进行指标统计 会自动合并
# 要解决的问题：如何分组 统计指标是什么
import numpy as np
import pandas as pd

# 创建一个分组df
index = ['stu_' + str(i) for i in range(6)]
df = pd.DataFrame(data={
    'cls_id': ['A', 'A', 'A', 'B', 'B', 'B'],
    'group_id': [1, 1, 1, 2, 1, 2],
    'name': ['zs', 'ls', 'ww', 'zl', 'xx', 'yy'],
    'height': [156, 189, 170, 176, 178, 179],
    'score': [90, 78, 99, 98, 86, 87]

},
    index=index)
print(df)

res = df.groupby(by='cls_id')['height'].max()
print(res)
# cls_id
# A    189
# B    179

# 按照班级进行分组 统计各个班级的身高 成绩平均值
# 按照单列进行分组 统计多列的指标
res = df.groupby(by='cls_id')[['height', 'score']].mean()
print(res)
# cls_id
# A       171.666667  89.000000
# B       177.666667  90.333333

# 按照班级、小组的学员的身高的最大值
# 按照多列进行分组，统计单列指标
res = df.groupby(by=['cls_id', 'group_id'])['height'].max()

print(res)
print(type(res))
# cls_id  group_id
# A       1           189
# B       1           178
#         2           179
# Name: height, dtype: int64
# <class 'pandas.core.series.Series'>

# res = df.groupby(by=['cls_id', 'group_id'])[['height', 'score']].max()
#
# print(res)
# cls_id group_id    height  score
# A      1            189     99
# B      1            178     86
#        2            179     98


# 可以求出多列的多个指标，无法分组

# print(df[['height', 'score']].agg([np.max, np.mean]))
#           height      score
# amax  189.000000  99.000000
# mean  174.666667  89.666667

print(df.agg({'height': [np.max, np.min], 'score': [np.mean]}))
#       height      score
# amax   189.0        NaN
# amin   156.0        NaN
# mean     NaN  89.666667
# NaN表示未求


# 使用transform只能实现agg自定义功能
print(df[['height', 'score']].transform(lambda x: x + 100))
