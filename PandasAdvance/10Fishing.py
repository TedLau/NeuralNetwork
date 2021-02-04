# 求品牌最火 就是求其销售额最高

# 销售额 -- 访问量*转化率 * 单价
import os
import time

import pandas as pd

# data = pd.read_excel('./data/垂钓装备&绑钩器.xlsx')
# print('data:\n', data)
#
# print(data['日期'].unique())
#
# # 计算销售额
# data['销售额'] = data.loc[:, '转化率'] * data.loc[:, '访客数'] * data.loc[:, '客单价']
# print('data:\n', data)
#
# # 按照品牌统计各个品牌的销售额
# res = data.groupby(by='品牌')['销售额'].sum().reset_index()
# print('res:\n', res)
#
# # 增加大的类目
# res.loc[:, '类目'] = '垂钓装备&绑钩器.xlsx'.replace('.xlsx', '')
# print('res:\n', res)


# 所有文件的统计数据

start = time.time()
# 获取所有文件名称
filenames = os.listdir('./data/')
print('filenames:\n', filenames)
# 创建一个新的空的df进行占位
df = pd.DataFrame()
# 循环加载并处理每个文件
for filename in filenames:
    # 加载文件
    file_data = pd.read_excel('./data/' + filename)
    print('file_data:\n', file_data)

    # 计算销售额
    file_data['销售额'] = file_data.loc[:, '转化率'] * file_data.loc[:, '访客数'] * file_data.loc[:, '客单价']
    print('file_data:\n', file_data)

    # 计算各个品牌的销售额
    res = file_data.groupby(by='品牌')['销售额'].sum().reset_index()
    res.loc[:, '类目'] = filename.replace('.xlsx', '')
    print('res:\n')

    # 将各个类目，各个品牌下的销售额进行合并 合并到df
    df = pd.concat((df, res), axis=0)

print('*' * 100)
print(df)

# 按照品牌进行分组，统计销售额的sum
res = df.groupby(by='品牌')['销售额'].sum().reset_index().sort_values(by='销售额', ascending=False).head(5)
print(res)
end = time.time()
print('花费时间为:{}s\n'.format(end - start))
