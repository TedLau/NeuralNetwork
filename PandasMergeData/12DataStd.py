import pandas as pd
import numpy as np


# 数据归约 剔除数量级的影响  以减少运算量 数据标准化
# 分类
# 离差标准化
#   将数据映射到一个小的范围[0,1]
#   new_x = (x - min) / (max - min)
#  min  max
# 特点：
# 转化之后，大依然大，小依然小
# 极差过大---分母过大---整体数据偏小，数据差异不明显
#       标准化后，要记录下最大值、最小值、计算原始数据使用
# 如果出现新的数据，不在之前的记录区间内，则转化后，会出现＞1的情况

# 实现离差标准化

def min_max_sca(data):
    data = (data - data.min()) / (data.max() - data.min())

    return data


# 加载detail数据
detail = pd.read_excel('./meal_order_detail.xlsx')
# 对amounts单价进行离差标准化
detail.loc[:, 'amounts'] = min_max_sca(detail.loc[:, 'amounts'])
print(detail.loc[:, 'amounts'])


# 标准差标准化
# 目前使用比较广泛的标准化的方式
# 将数据转为均值为0，标准差为1的数据，将数据转为服从过正态分布的数据
# new_x = (x - mean ) / std
# 特点
# 1、标准化之后的数据不局限在0-1，可以正负，均值为0标准差为1
# 2、不会影响数据的整体分布，大依然大

def get_std(val):
    val = (val - val.mean()) / val.std()
    return val


# 对amounts列进行标准化的转化
detail.loc[:, 'amounts'] = detail.loc[:, 'amounts'].transform(get_std)
print(detail.loc[:, 'amounts'])


# 小数定表标准化
#   通过移动小数点的位置来进行数据转化，将数据转为-1 - 1 之间
#   小数点移动的位数取决于该列数据绝对值的最大值
# new_x = x / 10 ^ k
# k ---- log10(|x|.max()) 向上取整 转为int

# 设有一列数据在-99 - 99 之间
# a 取绝对值最大值
# b 对最大值进行lg （1,2）之间的数字
# c 对（1，2）之间的向上取整
# d 转为int
# 根据公式 分母 =100 向左移动两位 ----> [-0.99,0.99]之间

# 特点：
# 将数据映射到-1 - 1
# 数据分布不变化、大依然大、小依然小


# 实现小数标准化

def desc_sca(data):
    data = data / (10 ** (int(np.ceil(np.log10(data.abs().max())))))
    return data


detail.loc[:, 'amounts'] = detail.loc[:, 'amounts'].transform(desc_sca)
print('小数标准化之后的结果:\n', detail.loc[:, 'amounts'])

# 离差标准化、小数定标标准化 容易收到异常值的影响
# 标准差标准化---异常值==对均值的英雄要比异常值对具体某个数的英雄要小的多
