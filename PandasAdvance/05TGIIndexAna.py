# 目标群体指数
# TGI指数 = [目标群体中具有某一特征的群体所占比例/总体中具有相同特征的群体所占比例 ] * 标准数100
# 用来表示某一地区中不同目标群体对于某问题的关心程度

import pandas as pd

# 加载数据
data = pd.read_excel('./TGI指数案例数据.xlsx')


# print('data:\n', data)
# print('data列索引:\n', data.columns)
#
# # 1、单个用户平均支付金额
#
# # 按照卖家昵称进行分组 实付金额 以及  退款
#
# # 需要球出订单状态 以及  各个对应的数量
# print('*' * 100)
# print(data['订单状态'].value_counts())
# # 交易成功                 27792
# # 付款以后用户退款成功，交易自动关闭     1040

# # 删除付款以后退款成功 交易自动关闭  删除法
# bool_mask = data.loc[:, '订单状态'] == '付款以后用户退款成功，交易自动关闭'
# # 确定退款的行名称
# index = data.loc[bool_mask, :].index
# # 删除
# data.drop(labels=index, axis=0, inplace=True)
# print('删除交易失败后的结果为:\n', data)
#

# 保留交易成功的订单
# a、确定哪些数据是交易成功的
# bool_mask = data.loc[:, '订单状态'] == '交易成功'
# data = data.loc[bool_mask, :]
# print("删除交易失败的结果为:\n", data)
#
# # 按照卖家昵称 进行分组 ----实付金额
# #  reset_index() 给数据修改新的索引
# print(data.groupby(by='买家昵称')['实付金额'].sum().reset_index())
#
#
# 根据实付金额判断是高客单还是低客单

def if_high(el):
    if el >= 50:
        return '高客户'
    else:
        return '低客户'


data.loc[:, '客户类别'] = data.loc[:, '实付金额'].transform(if_high)


def is_NaN(el):
    if el == 0:
        return 0.1
    else:
        return el


# bool_mask = data['高客户'] == 'NaN'

# data.loc[:, '高客户'] = data.loc[:, '高客户'].transform(is_NaN)
# print('data:\n', data)
# pd.set_option('display.max_rows', 100)pd.set_option('display.max_rows', 100)
# 利用透视表的方法来统计各个省市高客单还是低客单人数
res = pd.pivot_table(data=data,
                     index=['省份', '城市'],
                     columns='客户类别',
                     values='买家昵称',
                     aggfunc='count')

# print("res:\n", res.head(100))
# print(type())
# pd.set_option('display.max_rows', 100)
# res.loc[:, '高客户'] = res.loc[:, '高客户'].transform(is_NaN)
# print('*' * 100)
# print(res.head(100))
# res:  下单量
#  客户类别             低客户     高客户
# 省份   城市
# 上海   上海市      3209.0  2599.0
# 云南省  临沧市         3.0     3.0
#      丽江市         2.0     3.0
#      保山市         6.0     2.0
#      大理白族自治州     9.0    12.0
#               ...     ...
# 黑龙江省 绥化市        16.0     2.0
#      鸡西市         7.0     3.0
#      鹤岗市         1.0     2.0
#      黑河市         5.0     3.0
#      齐齐哈尔市      15.0    10.0

# 计算总人数以及每个城市对应的高客单占比
# 转为df

df = res.reset_index()
# # print(df)
#
# # 计算总单量 = 低客单 + 高客单
df['all'] = df['低客户'] + df['高客户']
# print(df['all'])
#
# # 各个城市的高客单 占该城市的单数比
df['percent_gao'] = df['高客户'] / df['all']
# print(df)
# 客户类别    省份       城市     低客户     高客户     all  percent_gao
# 0       上海      上海市  3209.0  2599.0  5808.0     0.447486
# 1      云南省      临沧市     3.0     3.0     6.0     0.500000
# 2      云南省      丽江市     2.0     3.0     5.0     0.600000
# 3      云南省      保山市     6.0     2.0     8.0     0.250000
# 4      云南省  大理白族自治州     9.0    12.0    21.0     0.571429
# ..     ...      ...     ...     ...     ...          ...
# 341   黑龙江省      绥化市    16.0     2.0    18.0     0.111111
# 342   黑龙江省      鸡西市     7.0     3.0    10.0     0.300000
# 343   黑龙江省      鹤岗市     1.0     2.0     3.0     0.666667
# 344   黑龙江省      黑河市     5.0     3.0     8.0     0.375000
# 345   黑龙江省    齐齐哈尔市    15.0    10.0    25.0     0.400000
# [346 rows x 6 columns]
# 计算全国高客单占比
#
percent_gao = df['高客户'].sum() / df['all'].sum()
# print(percent_gao)
# # 0.40999895771809747
#
#
# # 计算每个城市的高客单TGI占比
df['TGI_City'] = df['percent_gao'] / percent_gao * 100
print(df)
# 客户类别    省份       城市     低客户     高客户     all  percent_gao    TGI_City
# 0       上海      上海市  3209.0  2599.0  5808.0     0.447486  109.143259
# 1      云南省      临沧市     3.0     3.0     6.0     0.500000  121.951530
# 2      云南省      丽江市     2.0     3.0     5.0     0.600000  146.341835
# 3      云南省      保山市     6.0     2.0     8.0     0.250000   60.975765
# 4      云南省  大理白族自治州     9.0    12.0    21.0     0.571429  139.373177
# ..     ...      ...     ...     ...     ...          ...         ...
# 341   黑龙江省      绥化市    16.0     2.0    18.0     0.111111   27.100340
# 342   黑龙江省      鸡西市     7.0     3.0    10.0     0.300000   73.170918
# 343   黑龙江省      鹤岗市     1.0     2.0     3.0     0.666667  162.602039
# 344   黑龙江省      黑河市     5.0     3.0     8.0     0.375000   91.463647
# 345   黑龙江省    齐齐哈尔市    15.0    10.0    25.0     0.400000   97.561224
# [346 rows x 7 columns]


# 对TGI指数进行排序 降序
# 按照某列进行排序  默认升序 可以改变参数 ascending=False
df = df.sort_values(by='TGI_City', ascending=False)
print('*' * 100)
print(df)
# # ****************************************************************************************************
# 客户类别        省份         城市  低客户   高客户   all  percent_gao    TGI_City
# 149   新疆维吾尔自治区        哈密市  1.0   4.0   5.0     0.800000  195.122447
# 152   新疆维吾尔自治区  巴音郭楞蒙古自治州  3.0  10.0  13.0     0.769231  187.617738
# 136    广西壮族自治区        河池市  2.0   5.0   7.0     0.714286  174.216471
# 343       黑龙江省        鹤岗市  1.0   2.0   3.0     0.666667  162.602039
# 231        海南省    昌江黎族自治县  1.0   2.0   3.0     0.666667  162.602039
# ..         ...        ...  ...   ...   ...          ...         ...
# 293      西藏自治区        昌都市  NaN   1.0   NaN          NaN         NaN
# 294      西藏自治区        林芝市  NaN   1.0   NaN          NaN         NaN
# 295      西藏自治区       那曲地区  NaN   1.0   NaN          NaN         NaN
# 332        青海省    黄南藏族自治州  1.0   NaN   NaN          NaN         NaN
# 338       黑龙江省     大兴安岭地区  3.0   NaN   NaN          NaN         NaN
# [346 rows x 7 columns]


# 筛选出TGI数值较高，但是总单量较少的城市
#  高于平均单量

bool_mask = df['all'] > df['高客户'].mean()
df = df.loc[bool_mask, :]
df = df.loc[bool_mask, :]
df['TGI_City'] = df['percent_gao'] / percent_gao * 100
df = df.sort_values(by='TGI_City', ascending=False)
print('df:\n', df.head()[['省份', '城市']])
