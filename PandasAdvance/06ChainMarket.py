import pandas as pd

# 加载数据

order = pd.read_csv('./order.csv', encoding='ansi')
print('order:\n', order)

# 哪些商品比较畅销
# 计算各类商品 销量 排序
# 除去异常销量

# bool_mask = order['销量'] <= 0
# # 确定要删除的行名称
# index = order.loc[bool_mask, :].index
# order.drop(labels=index, axis=0, inplace=True)
# print('删除后的数据\n', order)
# res = order.groupby(by='类别ID')['销量'].sum().reset_index().sort_values(by='销量', ascending=False)['类别ID'].head(100)
#
# print(res)

res = pd.pivot_table(data=order,
                     index='类别ID',
                     values='销量',
                     aggfunc='sum').reset_index().sort_values(by='销量', ascending=False).head(10)
print(res)

# 哪些商品比较畅销
res = pd.pivot_table(data=order,
                     index='商品ID',
                     values='销量',
                     aggfunc='sum').reset_index().sort_values(by='销量', ascending=False).head(10)
print(res)

# 求不通门店的销售额占比
# 单价 * 销量 -----商品的销售额
# 按照门店进行分组 统计商品具体的销售额 之和
# 占比 各门店 /  销售总和

order.loc[:, '销售额'] = order.loc[:, '单价'] * order.loc[:, '销量']

# 按门店进行分组
res = order.groupby(by='门店编号')['销售额'].sum().reset_index()
print(res)

# 算占比
print('各个占比\n', res['销售额'] / res['销售额'].sum())

# 哪个时间段是高峰期？
# 给定的数据需要划分 按照时间进行划分 每个小时可以认为是一个时间段
# 统计的是各个时间段内 不同订单id出现的次数  越多认为客流量大
# 假设一个订单对应一个人

# 将时间转为pandas默认支持的时间
order.loc[:, '成交时间'] = pd.to_datetime(order.loc[:, '成交时间'])
# 使用列表推导式
order['hour'] = [i.hour for i in order.loc[:, '成交时间']]

# 去掉不同的订单 去重
# unique np
# drop_duplicate df
# subset 表示去重的列
# keep=’first‘ 默认保存第一次出现的数据
order.drop_duplicates(subset='订单ID', inplace=True)

# 按照hour进行分组 统计订单ID在各个小时内出现的次数
res = order.groupby(by='hour')['订单ID'].count().sort_values(ascending=False)
print('res:\n', res)
