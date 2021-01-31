import pandas as pd

print('aaa')
detail = pd.read_excel('./meal_order_detail.xlsx')
print('detail:\n', detail)
print('detail:\n', detail.columns)

# 多列返回dataframe 单列series
print('获取多列数据:\n', detail[['dishes_name', 'itemis_add', 'counts', 'amounts']])

# 获取前n行 行下标切片 行名称切片也可以(包含尾部)  行下标列表也可以 [0,1,2,3,112]  head前n行 默认5 tail后n行
print('单列数据:\n', detail['dishes_name'][:10])
