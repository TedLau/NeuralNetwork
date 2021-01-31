import pandas as pd

# 使用loc  iloc同时对行列进行索引

# 加载数据
detail = pd.read_excel('./meal_order_detail.xlsx')
print('Deatil:\n', detail)

print('列索引:\n', detail.columns)
# 对索引重新赋值
index = ['index_' + str(i) for i in detail.index]
detail.index = index
# loc :只能使用名称
# 获取 dishes_name

print('获取单列数据:\n', detail.loc[:, 'dishes_name'])
# 获取多列使用列名 列表 指定行
print('多列指定行:\n', detail.loc['index_2770':'index_2778', 'dishes_name'])

# iloc 只可以使用下标
print('获取单列数据:\n', detail.iloc[:, 5])  # 与上面的获取dishes_name一样



# 先列后行效率高 直接索引方式
# 大多数平台会封装 iloc loc
