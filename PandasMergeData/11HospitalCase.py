import pandas as pd

# 加载数据
data = pd.read_excel('./某医院2018年数据.xlsx')
print('data:\n', data)
print('data的列索引\n', data.columns)
print('每一列的非空数据的数量:\n', data.count())

# 每一列的非空数据的数量:
#  购药时间    6576
# 社保卡号    6576
# 商品编码    6577
# 商品名称    6577
# 销售数量    6577
# 应收金额    6577
# 实收金额    6577

# 先进性数据处理
# 先进性数据清洗：
# 给列索引更名
# 购药时间 --成交时间
# 更改列索引
data.rename(columns={'购药时间': '成交时间'}, inplace=True)
print('更改之后的数据:\n', data.columns)

# 删掉所有空的数值
#   删掉所有具有空值的行
data.dropna(axis=0, how='any', inplace=True)
# 将销售数量、应收金额、实收金额数据类型改为int
# 获取原来的每一列的数据类型
print('原来的数据类型:\n', data.dtypes)
# 修改类型  astype
data.loc[:, ['销售数量', '应收金额', '实收金额']] = data.loc[:, ['销售数量', '应收金额', '实收金额']].astype('int')
print('修改数据类型后的结果为:\n', data.dtypes)
# 原来的数据类型:
#  成交时间     object
# 社保卡号    float64
# 商品编码    float64
# 商品名称     object
# 销售数量    float64
# 应收金额    float64
# 实收金额    float64
# dtype: object
# 修改数据类型后的结果为:
#  成交时间     object
# 社保卡号    float64
# 商品编码    float64
# 商品名称     object
# 销售数量      int32
# 应收金额      int32
# 实收金额      int32


# 删除 '销售数量', '应收金额', '实收金额' 小于0 的数据
# 根据具体业务剔除 异常值 -----自己设置函数
# 利用保留法 销售数量》 0 应收金额 》0 实收金额 》0
# 利用bool数组
bool_mask1 = data.loc[:, '销售数量'] > 0
bool_mask2 = data.loc[:, '应收金额'] > 0
bool_mask3 = data.loc[:, '实收金额'] > 0
bool_mask = bool_mask3 & bool_mask2 & bool_mask1

# 删除
data = data.loc[bool_mask, :]
print('删除掉之后的数据为:\n', data)


# 成交时间格式修改


def get_time1(val):
    """

    :param val:
    :return:
    """
    val = val.split(' ')[0]
    if val == '2018-02-29':
        val = '2018-02-28'
    val = pd.to_datetime(val)

    return val


data.loc[:, '成交时间'] = data.loc[:, '成交时间'].transform(get_time1)
print('修改后的时间数据为:\n', data)
print('修改时间时间数据后的类型:\n', data.dtypes)

print()
# 分析
# （1）每个月的人流量？
# 获取月份
data.loc[:, 'month'] = [i.month for i in data.loc[:, '成交时间']]
# 同一个社保卡对应一个人，每一个具体的成交时间对应一个人
# 同一个社保卡号，在不同的时候，算不同的流量
# 需要对社保卡号、成交时间进行去重
res = data.loc[:, ['month', '成交时间', '社保卡号']].drop_duplicates(subset=['社保卡号', '成交时间'], inplace=False)
# 按照月进行分组 month 统计行数
res_flow = res.groupby(by='month')['社保卡号'].count()
print('res_flow:\n', res_flow)
# （2）人均平均消费

# 计算人数
# 可以对比社保卡号进行去重，计算不同的社保卡号的消费，则可以得到人均消费
cnts = data.drop_duplicates(subset='社保卡号', inplace=False).shape[0]
# 计算总的销售额
all_in = data.loc[:, '实收金额'].sum()
# 计算人均消费
print('人均消费为:\n', all_in / cnts)


# （3）计算使用次数最多的次数
# 直接计算不同的商品名称出现的次数
# 按照名称进行分组。统计各个组内的销售数量的sum
res = data.groupby(by='商品名称')['销售数量'].sum().reset_index().sort_values(by='销售数量', ascending=False).head(10)
print('res:\n', res)

# （4）多少人办卡
print('cnts:\n', cnts)
