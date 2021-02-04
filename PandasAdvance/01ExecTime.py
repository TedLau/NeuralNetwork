import pandas as pd

# 加载数据
detail = pd.read_excel('./meal_order_detail.xlsx')

print('detail:\n', detail)
print('列索引:\n', detail.columns)

# 获取place_order_time

print(detail.loc[:, 'place_order_time'])

# 转为pandas默认支持的时间序列
detail.loc[:, 'place_order_time'] = pd.to_datetime(detail.loc[:, 'place_order_time'])

# 获取对应的时间属性
_unit_map = {
    "year": "year",
    "years": "year",
    "month": "month",
    "months": "month",
    "day": "day",
    "days": "day",
    "hour": "h",
    "hours": "h",
    "minute": "m",
    "minutes": "m",
    "second": "s",
    "seconds": "s",
    "ms": "ms",
    "millisecond": "ms",
    "milliseconds": "ms",
    "us": "us",
    "microsecond": "us",
    "microseconds": "us",
    "ns": "ns",
    "nanosecond": "ns",
    "nanoseconds": "ns",
}
# year
detail.loc[:, 'year'] = [i.year for i in detail.loc[:, 'place_order_time']]
print('year:\n', detail.loc[:, 'year'])

# 时间差计算


# 默认支持时间点类型之间的差值计算

res = pd.to_datetime('2021-7-13') - pd.to_datetime('2021-2-1')
print(res)
# 162 days 00:00:00
print(type(res))
# <class 'pandas._libs.tslibs.timedeltas.Timedelta'>  时间差计算类型 德塔 跟数学差不多的那个
print(res.days)  # 162

print(pd.to_datetime('2021-2-1') + pd.Timedelta(days=200))  # 计算200天后的日期 最大的是周week
# 2021-08-20 00:00:00
