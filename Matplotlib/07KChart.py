# K线图 金融领域 股票走势
# 开盘价 最高价 最低价 收盘价
# 开盘 > 收盘 价格下跌 绿色表示
# 开盘 < 收盘 价格上涨 红色表示

import matplotlib.pyplot as plt
import mpl_finance as mpl

import numpy as np
import tushare as ts

# 创建画布
fig = plt.figure()

data = ts.get_k_data('600728', ktype='D', start='2020-10-4', end='2021-1-26', autype='qfq')
print('data:', data)

# 筛选数据 ohlc
prices = data[['open', 'high', 'low', 'close']]

print('Prices:\n', prices)
dates = data['date']
print('Dates:\n', dates)

# 合并数据

candledata = np.column_stack((list(range(len(dates))), prices))
print(candledata)
# 获取坐标系  参数 左间距 下间距 图形宽度 图形高度
ax = fig.add_axes([0.1, 0.3, 0.8, 0.6])
mpl.candlestick_ohlc(ax, candledata, width=0.5, colorup='r', colordown='g')
plt.show()
