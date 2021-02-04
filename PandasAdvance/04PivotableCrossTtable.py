import numpy as np
import pandas as pd

# 透视表 高级版的分组聚合 分组聚合全部可以使用透视表来替代

# 可以使用pd.pivot_table 创建透视表
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

# 　按照班级进行分组　统计各个班级身高的最大值
print(df.groupby(by='cls_id')['height'].max())

# data 创建透视表的数据
# values 关心的主体
# index 按照index指定的列进行分组 结果的index
# aggfunc  对关心主体的统计指标
res = pd.pivot_table(data=df,
                     values='height',
                     index='cls_id',
                     aggfunc='max')
# 返回结果跟pandas版本有关 有可能是dataframe也可能是series
print(res)
#         height
# cls_id
# A          189
# B          179


# 创建透视表
# 按照指定其列的名称 进行列分组
res = pd.pivot_table(data=df,
                     index='cls_id',
                     aggfunc='max',
                     columns='group_id')
print(res)
#          height        name      score
# group_id      1      2    1    2     1     2
# cls_id
# A         189.0    NaN   zs  NaN  99.0   NaN
# B         178.0  179.0   xx   zl  86.0  98.0

# 交叉表
# pd.crosstab 交叉表
# index  结果的行索引
# columns  结果的列索引
# 在满足行列的条件下 出现数据的次数

res = pd.crosstab(index=df['height'],
                  columns=df['score'])
print('res:\n', res)

# res:
#  score   78  86  87  90  98  99
# height
# 156      0   0   0   1   0   0
# 170      0   0   0   0   0   1
# 176      0   0   0   0   1   0
# 178      0   1   0   0   0   0
# 179      0   0   1   0   0   0
# 189      1   0   0   0   0   0


# values 关心的主体
# aggfunc 统计的指标
# index 和 columns 必须同时出现
# values 和 aggfun必须同时出现
res = pd.crosstab(index=df['cls_id'],
                  columns=df['group_id'],
                  values=df['height'],
                  aggfunc=np.max)
print('res:\n', res)

# res:
#  group_id      1      2
# cls_id
# A         189.0    NaN
# B         178.0  179.0
