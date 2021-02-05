import pandas as pd
import numpy as np
from scipy.interpolate import interp1d, lagrange  # 线性插值 拉格朗日插值

# 缺失值 空缺了

# 判断是否存在缺失的值

# 加载数据
data = pd.read_excel('./qs.xlsx')
print('data:\n', data)

# 缺失值检测
# isnull -- 判定 如果是缺失值，则True 不是则False  ye也麻烦，和sum连用 统计各个列的缺失值
# notnull相反
# print('缺失值检测:\n', pd.isnull(data).sum())
# 缺失值检测:
#  商品ID    2
# 类别ID    2
# 门店编号    2

# 缺失值处理方式
# 1、删除法
# drop 删除指定的列
# dropna 删除缺失值
data = data
# how any存在缺失值就删除该行 all  则全部才删除
# data = data.dropna(axis=1, how='any', inplace=False)
print('data:\n', data)
# 以上数据出现empty dataframe
# 一般不随意使用
# 2、填充法
# 利用指标数据进行填充
# 可以使用众数、均值、中位数或者其临近数值填充
# 可以对类别型数据进行填充众数

# 使用上邻居进行填充
# ffil pad 表示上一个非缺失的值
# backfill bfill 下一个非缺失的值
data.loc[:, '类别ID'].fillna(method='pad', inplace=True)
# 尝试使用众数来填充 商品id 这列数据

# 1、计算众数
mode = data.loc[:, '商品ID'].mode()[0]
# 2、进行填充
data.loc[:, '商品ID'].fillna(value=mode, inplace=True)
print('填充之后的结果为:\n', data)

# 3、插值法
# 线性插值
# d多项式插值
# 样条插值

# 创建插值数据
# 用现有数据去拟合未知的数据
x = np.array([1, 2, 3, 4, 5, 6, 8])
y = np.array([3, 5, 6, 9, 11, 13, 15])
z = np.array([2, 8, 18, 32, 50, 128, 162])
# 使用x 来分别用线性插值 拉格朗日插值拟合

# 线性插值
# x 用来拟合的数据
# y 需要被拟合的数据
linear = interp1d(x=x, y=y, kind='linear')  # 线性插值

print('使用线性拟合来拟合数据:\n', linear([1, 7]))  # [17. 19.]  输出的是y的坐标，就是在x给定情况下，预测y的值

# 拉格朗日插值
# 使用x 借助拉格朗日插值多项式来拟合yz
# 拉格朗日插值模块
# x 用来拟合的数据
# w 需要被拟合的数据
la1 = lagrange(x=x, w=y)
print('使用拉格朗日插值拟合的数据为:\n', la1([6, 7]))
