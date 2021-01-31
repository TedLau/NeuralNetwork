import numpy as np
import pandas as pd

# 基于numpy 能够存储表格数据 统计分析 数据清洗
# 数据分析 挖掘数据库

# DataFrame ---结构  具有行索引 也具有列索引
# 数据处理 数据清洗 数据集成 数据规约 数据变换

# 存储数据的  两种结构

# 创建df --列表嵌套

# data = [['zs', 19, 2],
#         ['as', 12, 2]]
#
# df = pd.DataFrame(data=data,
#                   index=['S0', 'S1'],
#                   columns=['name', 'age', 'group']
#                   )
# print('df:\n', df)
#
# # 创建df  --使用大字典
# df = pd.DataFrame(
#     data={
#         'name': ['ls', 'ws'],
#         'age': [12, 23],
#         'group': [2, 3]
#
#     },
#     index=['s0', 's1']
# )
# print(df)

# res = np.load('./gdp.npz', allow_pickle=True)
#
# # 获取数组
# columns = res['columns']
# values = res['values']
# print('Column:\n', columns)
# print('Values:\n', values)
#
# # 构建行索引名称
# index = ['index' + str(i + 1) for i in range(values.shape[0])]
# df = pd.DataFrame(data=values,
#                   columns=columns,
#                   index=index
#                   )
# print('df\n', df)

# Series --只有行索引  数据的表格结构
#          数据的类型都是一致

# 简单列表  一维数组创建series
# se = pd.Series(data=['zs', 'ls'],
#                )  默认index为0 1
# print(se)
# 0    zs
# 1    ls

# se = pd.Series(data=np.array(['zs','ls']),
#                index=['s1','s2'])
# print(se)
#   指定的index
# s1    zs
# s2    ls

# df中的一列为series 多个series可以组成dataframe

# 通过映射关系创建series 并按照index进行排序
#  这种会使用index在score里找对应的元素，如果有则为值，如果没有找到，那么便为NaN
scores = {'zs': 90, 'ls': 91, 'lpw': 100}
index = ['zs', 'ls', 'ww']
se = pd.Series(data=scores, index=index)
print(se)
