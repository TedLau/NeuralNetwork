import pandas as pd
import seaborn as sns
 # 测试失败
# 加载数据
anscombe = sns.load_dataset('anscombe')
print('anscombe:\n', anscombe)
print('*' * 100)

# # 将数据拆分为 四部分
# # 如果获取 dataset == IV
# # bool数组
# bool_mask = anscombe.loc[:, 'dataset'] == 'IV'
# # 筛选第四部分
# df4 = anscombe.loc[bool_mask, :].reset_index().drop(labels=['index', 'dataset'], axis=1, inplace=False)
# print(df4)

# 数据集拆分
df1 = anscombe.loc[anscombe.loc[:, 'dataset'] == 'I', :].reset_index().drop(labels=['index', 'dataset'], axis=1,
                                                                            inplace=False)
df2 = anscombe.loc[anscombe.loc[:, 'dataset'] == 'II', :].reset_index().drop(labels=['index', 'dataset'], axis=1,
                                                                             inplace=False)
df3 = anscombe.loc[anscombe.loc[:, 'dataset'] == 'III', :].reset_index().drop(labels=['index', 'dataset'], axis=1,
                                                                              inplace=False)
df4 = anscombe.loc[anscombe.loc[:, 'dataset'] == 'IV', :].reset_index().drop(labels=['index', 'dataset'], axis=1,
                                                                             inplace=False)
print('df1:\n', df1)
print('df2:\n', df2)
print('df3:\n', df3)
print('df4:\n', df4)
print('*' * 100)
# 进行主键合并 按照行索引值相同进行合并 left_index=True right_index=True
