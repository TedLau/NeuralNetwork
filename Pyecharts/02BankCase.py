import pandas as pd

# 加载数据
data = pd.read_csv('./loan.csv')
print('data:\n', data)

# 1、是否收入越高，坏账率越高
# 研究--收入--好坏用户的数量
# 按照月收入进行分组，统计各个月收入区间内 坏用户的数量
# 检测缺失值
res_null = pd.isnull(data).sum()
# 删除、填充、插值
# 使用众数，来填充
mode = data.loc[:, '月收入'].mode()[0]
print('月收入的mode:\n', mode)
# 填充
data.loc[:, '月收入'].fillna(value=mode, inplace=True)
print('data  :\n', data)

# 对月收入进行分组 -离散数据进行分组
# 月收入是连续的小数的值，直接进行分组，每个值都是一组
# 默认分组
res_cut = pd.cut(x=data.loc[:, '月收入'],
                 bins=5)
print('res:\n', res_cut)
# 2、计算年龄和坏账率有什么关系
# 3、计算家庭人口数量和坏账率的关系
