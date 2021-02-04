import pandas as pd

# 加载数据

detail = pd.read_excel('./meal_order_detail.xlsx')
print('列索引:\n', detail.columns)

# 转为pandas可以支持的时间属性
detail.loc[:, 'place_order_time'] = pd.to_datetime(detail.loc[:, 'place_order_time'])

# 添加一列day

detail['day'] = [i.day for i in detail.loc[:, 'place_order_time']]

# 计算每日销售额

detail['payT'] = detail.loc[:, 'counts'] * detail.loc[:, 'amounts']

print('detail:\n', detail)
# 分组
# 表明的是求payT列的和
res = detail.groupby(by='day')['payT'].sum()
print(res)
