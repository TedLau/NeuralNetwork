import pandas as pd

# 加载数据

detail = pd.read_excel('./meal_order_detail.xlsx')
print('数据:\n', detail)
print('列名:\n', detail.columns)

# 对detail中的 amounts 列进行统计指标

# max min mean median
# std标准差 var方差 ptp极差 idmax最大值下标 idmin最小值下标

# print('获取amounts列的标准差：', detail.loc[:, 'amounts'].std())
# print('获取amounts列的方差：', detail.loc[:, 'amounts'].var())
# print('获取amounts列的极差：', detail.loc[:, 'amounts'].ptp())  # max 178 - min 1
# print('获取amounts列的最大值下标：', detail.loc[:, 'amounts'].idxmax())
# print('获取amounts列的最小值下标：', detail.loc[:, 'amounts'].idxmin())

print('amounts列最大值', detail.loc[:, 'amounts'].max())
# amounts列最大值 178

print('amounts列标准差', detail.loc[:, 'amounts'].std())

print('amounts列方差', detail.loc[:, 'amounts'].var())

# print('amounts列极差', detail.loc[:, 'amounts'].ptp())

print('amounts列最大值下标', detail.loc[:, 'amounts'].idxmax())

print('获取众数:\n', detail.loc[:, 'amounts'].mode())  # [0]获取具体的数值
#  0    35    0多35个
# dtype: int64


# count 非空数据的数量


# quantile ---分位数 默认百分50

print('获取amounts中的分位数:\n', detail.loc[:, 'amounts'].quantile())  # q = 不同的数组

# describe ---统计描述 一次可以统计出多个结果

print('获取amounts列的统计描述:\n', detail.loc[:, 'amounts'].describe())

# 获取amounts列的统计描述:    数值型
#  count    2779.000000
# mean       45.337172
# std        36.808550
# min         1.000000
# 25%        25.000000
# 50%        35.000000
# 75%        56.000000
# max       178.000000
# Name: amounts, dtype: float64

# describe 非数值型

print('非数值型:\n', detail.loc[:, 'dishes_name'].describe())

# 非数值型:
#  count      2779
# unique      154
# top       白饭/大碗
# freq         92
# Name: dishes_name, dtype: object


# 数值型统计出现频率可以使用astype('category')转为类别型
detail.loc[:, 'amounts'] = detail.loc[:, 'amounts'].astype('category')
print('非数值型:\n', detail.loc[:, 'amounts'].describe())
#  count     2779
# unique      55
# top         35
# freq       239
# Name: amounts, dtype: int64