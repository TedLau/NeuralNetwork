import pandas as pd
from scipy.interpolate import interp1d, lagrange
import numpy as np

# 使用拉格朗日进行插值计算
# 加载数据
data = pd.read_excel('./qs.xlsx')
print('data:\n', data)

# 确定前后多少个数据来进行构建拉格朗日插值关系
n = 5

# 循环查看缺失值的位置
for i in range(data.shape[0]):
    # i 代表行下标
    # print(i)
    # 判断如果是缺失值就进行插值
    if np.isnan(data.iloc[i, 1]):
        # print(i)
        # 获取 缺失值的前后n个数据
        if i - n <= 0:
            start = 0
        else:
            start = i - n

        mask = data.iloc[start:i + n, 1]
        # 获取已知的序列  以index为已知的序列x
        x = mask.index
        # 在x中剔除缺失位置的x
        # mask.notnull()
        x = x[mask.notnull()]
        # print(mask)
        # 获取y
        y = mask[mask.notnull()].values
        la = lagrange(x=x, w=y)
        # 拟合
        data.iloc[i, 1] = la([i])

print('插值后的结果:\n', data)
