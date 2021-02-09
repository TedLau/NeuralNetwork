import pandas as pd

import numpy as np

import json

# （1）电影类型如何随着时间的推移发生变化的？
# （2）电影类型与利润的关系？
# （3）Universal 和 Paramount 两家影视公司的对比情况如何？
# （4）改编电影和原创电影的对比情况如何？
# （5）电影时长与电影票房及评分的关系？
# （6）分析电影关键字


# 加载数据
credits = pd.read_csv('./tmdb_5000_credits.csv')
movies = pd.read_csv('./tmdb_5000_movies.csv')
# 查看数据集


print('credit:\n', credits.head())
print('credit columns:\n', credits.columns)
print('*' * 100)

print('movies:\n', movies.head())
print('movies columns:\n', movies.columns)

# 1、合并数据集
credits.rename(columns={'movie_id': 'id'}, inplace=True)
print('credit columns:\n', credits.columns)
# 根据电影id和title 将二者合并
data = pd.merge(left=credits, right=movies, on=['id', 'title'], how='outer')

# 获取合并后的电影信息

print('data columns:\n', data.columns)
print('data shape:\n', data.shape)

# 检测缺失值
res_nul = pd.isnull(data).sum()
print('res_nul:\n', res_nul)

# 获取缺失电影的名称
bool_mask_name_nul = pd.isnull(data.loc[:, 'release_date'])
# 显示确实电影名称
movies_names = data.loc[bool_mask_name_nul, 'original_title'].values[0]
print('movies_names:\n', movies_names)
# America Is Still the Place

# 首映日填充
data.loc[bool_mask_name_nul, 'release_date'] = '2014-06-01'
# 获取丢失时长的电影
bool_mask_runtime = pd.isnull(data.loc[:, 'runtime'])
movie_unruntime = data.loc[bool_mask_runtime, 'original_title'].values
print('movies unnames:\n', movie_unruntime)
# movies unnames:
#  ['Chiamatemi Francesco - Il Papa della gente'
#  'To Be Frank, Sinatra at 100']


# # 时间的缺失数据 给填充上
data.loc[data.loc[:, 'original_title'] == 'Chiamatemi Francesco - Il Papa della gente', 'runtime'] = 94.0
data.loc[data.loc[:, 'original_title'] == 'To Be Frank, Sinatra at 100', 'runtime'] = 81.0

# 检测缺失值
res_nul = pd.isnull(data).sum()
print('res_nul:\n', res_nul)

# 获取电影类型数据
print('genres:\n', data.loc[:, 'genres'].head())

# 将json类型转为python类型 json loads
# json.dumps  python转json
data.loc[:, 'genres'] = data.loc[:, 'genres'].transform(json.loads)
# 获取电影类型
type_set = set()


def get_movie_type1(elem):
    """
    自定义获取电影类型
    :param elem:
    :return:
    """
    # list存储类型
    type_list = []
    if elem:
        for i in elem:
            # 获取电影类型
            movie_type = i['name']
            # 添加到list
            type_list.append(movie_type)
            # 添加至type_set
            type_set.add(movie_type)
    return ' '.join(type_list)


def get_movie_type(element):
    """
    自定义获取电影类型
    :param element: 电影类型
    :return:
    """
    # type_list  --存储 该电影的类型
    type_list = []
    if element:
        for tmp in element:
            # 获取电影类型
            movie_type = tmp['name']
            # 将其添加 到
            type_list.append(movie_type)

            # 需要将其加入到 type_set
            type_set.add(movie_type)

    # 返回一个字符串
    return ' '.join(type_list)


# 处理genres
data.loc[:, 'genres'] = data.loc[:, 'genres'].transform(get_movie_type)

print('电影类型:\n', data.loc[:, 'genres'])

# 打印所有的电影类型

print('电影类型:\n', data.loc[:, 'genres'])

# 打印set

print('type_set:\n', type_set)

#  如果包含 类型 中的一个就置为1，不包含就0

for movie_type in list(type_set):
    data.loc[:, movie_type] = data.loc[:, 'genres'].str.contains(movie_type).transform(lambda x: 1 if x else 0)
print(data.shape)
print('data　columns:\n', data.columns)

# 获取类型与时间的变化

# 获取年份
# data.loc[:, 'release_year'] = pd.to_datetime(data.loc[:, 'release_date']).dt.year
#
# # 根据年份统计次数
# res = data.groupby(by='release_year')[list(type_set)].sum()
# print('res:\n', res)

data.loc[:, 'release_year'] = pd.to_datetime(data.loc[:, 'release_date']).dt.year

# 根据 年限 ---对 所有不同的电影统计出现的次数
res = data.groupby(by='release_year')[list(type_set)].sum()
print(res)
print('*' * 100)
