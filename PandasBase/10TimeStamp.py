import pandas as pd

# 关于时间的数据
res = pd.to_datetime('2021-1-31')
print(res)
print(type(res))

# 2021-01-31 00:00:00
# <class 'pandas._libs.tslibs.timestamps.Timestamp'>

# ['2020-10-9','2020-10-10']
# 多个时间字符串 时间序列 也可以使用to_datetime  DatetimeIndex pandas 中

# numpy中的时间类型  datetime64[ns]

# 只能是序列   可以通过DatetimeIndex将时间字符串序列转为pandas默认支持的时间序列



#可以通过获取pandas中默认支持的时间点 ，时间序列用来获取时间数据中的时间属性
# 列表推导式来获取