import pandas as pd
import numpy as np


# 订单详情表
# 订单信息表
# 用户表

# 合并订单详情表，订单信息表，用户表

det1 = pd.read_excel('./meal_order_detail.xlsx', sheet_name=0)
det2 = pd.read_excel('./meal_order_detail.xlsx', sheet_name=1)
det3 = pd.read_excel('./meal_order_detail.xlsx', sheet_name=2)

# 获取不同的索引列
print('det1:\n', det1.columns)
print('det2:\n', det2.columns)
print('det3:\n', det3.columns)

# 将三个不同的det合并为一个大的det
# 纵向堆叠 横向根据join
det = pd.concat((det1, det2, det3), axis=0)

print('res:\n', det.shape)

# 　加载ｉｎｆｏ
info = pd.read_csv('./meal_order_info.csv', encoding='ansi')
# 可以认为det中的order_id 与 info中的info_id都是表示的订单号
# 主键拼接
det_info = pd.merge(left=det, right=info, left_on='order_id', right_on='info_id', how='inner')

users = pd.read_excel('./users.xlsx')
# 可以使用users中的account与 info 中的name是 姓名
# 进行主键拼接 inner 避免失去太多数据
all_df = pd.merge(left=det_info, right=users, left_on='name', right_on='ACCOUNT', how='inner')

# print('all_df:\n', all_df)

print('all_columns:\n', all_df.columns)

# 判断 'emp_id_y'  与 'emp_id_x'  是否相等

# 使用numpy中的np.all
res = np.all((all_df['emp_id_x'] == all_df['emp_id_y']))
print("res:\n", res)
#  True  删除中的一些 相同的列的

all_df.drop(labels=['emp_id_y', 'ACCOUNT'], axis=1, inplace=True)
print('all_df:\n', all_df)

# 剔除整列为空的数据
drop_list = []
for column in all_df.columns:
    # 统计每一列非空数据的数量
    res = all_df.loc[:, column].count()
    # 判断值
    if res == 0:
        drop_list.append(column)

all_df.drop(labels=drop_list, axis=1, inplace=True)
print('删除整列为缺失数据的结果为:\n', all_df)

drop_list = []
# 删除整列数据一样的数据
# drop_duplicate  如果去重后只剩一个数据，则该列数据都一样
for column in all_df.columns:
    # 对每个数据进行去重，不进行修改
    res = all_df.drop_duplicates(subset=column, inplace=False)

    # 如果只剩一个数据，则只有一行
    if res.shape[0] == 1:  # 只剩一个数据则为 (1,)所以可以如此
        # 认为该列的值一样
        drop_list.append(column)

print('整列数据一样的有:\n', drop_list)

# 去除
all_df.drop(labels=drop_list, axis=1, inplace=True)
print('删除一样的结果后为:\n', all_df)
