import pandas as pd
import numpy as np

# 将特定的数据  转化为 可以使用的数据---数据变换
# 两种情况：
# 　1、将非数值型数据 转为数值型（哑变量变化

#
# df = pd.DataFrame(
#     data={
#         '城市': ['北京', '郑州', '西安']
#     }
# )
# print('df:\n', df)
# print('df type :\n', type(df))
#
# # data :需要转化的数据
# # prefix 转化后列名称的前缀
# # prefix_sep ：转化之后前缀与数据的连接符
#
# city_data = pd.get_dummies(data=df.loc[:, '城市'],
#                            prefix='city',
#                            prefix_sep='_')

# print('转化之后的数据:\n', city_data)

# 按照原来数据中的顺序进行排列，但是在转化后的列表中，显示的是按照音标顺序
# df:
#     城市
# 0  北京
# 1  郑州
# 2  西安
# df type :
#  <class 'pandas.core.frame.DataFrame'>
# 转化之后的数据:
#     city_北京  city_西安  city_郑州
# 0        1        0        0
# 1        0        0        1
# 2        0        1        0


#  2、将连续的小数数据--- 区间数据 离散化
# 将连续的小数数据---拆分成不同的区间
# cut -- 拆分
# detail ---amounts 单价数据----可以理解为连续的小数数据
# 将amounts进行拆分--离散化
detail = pd.read_excel('./meal_order_detail.xlsx')
print('data:', detail)
print('amounts:\n', detail.loc[:, 'amounts'].max())
# x : 需要离散化的数据
# bins: 分组的组数 分组节点
# include_lowest 默认false 如果系统默认拆分，包含最小值
# 如果自定义划分分组节点--- 不包含最小值，需要将include_lowest =True
res = pd.cut(x=detail.loc[:, 'amounts'],
             bins=5,
             include_lowest=True)

# 原来具体的值--各个区间来代替
print('res:\n', res)

# 可以通过value_counts(res)来看

print('cnts:\n', pd.value_counts(res))

# cnts:
#  (0.822, 36.4]     1488
# (36.4, 71.8]       885
# (71.8, 107.2]      233
# (142.6, 178.0]     130
# (107.2, 142.6]      43


# 自定义分组
# 1、自己直接指定给分组节点
bins = [1, 40, 80, 120, 160, 180]
res = pd.cut(x=detail.loc[:, 'amounts'],
             bins=bins,
             include_lowest=True)
print('res:\n', res)
print('*' * 100)
# 2、等宽分组
#   1、确定分组组数
group_num = 5
#   2、确定间距
# 确定最大值
max_am = detail.loc[:, 'amounts']
# 确定最小值

#   3、确定分组节点
# 3、等频分组
# 使用等宽分组，防止部分区间内不存在数据
bins = detail.loc[:, 'amounts'].quantile(q=np.arange(0, 1 + 1 / group_num))
print('bins:\n', bins)
