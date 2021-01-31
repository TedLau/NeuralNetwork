# 如果整列数据都是一样的 ---> 不同的数据在该列的表现都是一样

# 如果整列数据都是缺失的 --->整列数据对结果毫无意义 ---删除
import pandas as pd

detail = pd.read_excel('./meal_order_detail.xlsx')
print('detail:\n', detail)
print('detail的列索引：\n', detail.columns)

# 以 detail表为例，删除detail中整列都是缺失的 这些列
# 暂时无法判断整列都是缺失的
# 我们可以统计出整列数据中的非空数据的数目
# 如果你统计出来某列的数据的 非空数据的数目 = 0 --->说明整列数据 都是缺失的


# 删除法
# # 定义一个删除列表
# drop_list = []
#
# for column in detail.columns:
#     # 对每一列进行统计 count
#     res = detail.loc[:, column].count()
#     if res == 0:
#         # 将 column 加入到 drop_list
#         drop_list.append(column)
#
# # drop_list --->需要删除的列的名称列表
# print('drop_list：\n', drop_list)
# print('*' * 100)
#
# # 删除法
# detail.drop(labels=drop_list, axis=1, inplace=True)
# print('删除整列数据为空的之后的结果为：\n', detail)

# # 保留法
# # 保留 整列至少含有一个数据的列
# # 构建保留的列表
# save_list = []
#
# for column in detail.columns:
#     # 对每一列进行统计 count
#     res = detail.loc[:, column].count()
#     # 判断
#     if res > 0:
#         # 将column加入到 save_list
#         save_list.append(column)
#
# print('save_list:\n', save_list)
#
# # 筛选
# detail = detail.loc[:, save_list]
# print('删除整列为空的结果：\n',detail)
