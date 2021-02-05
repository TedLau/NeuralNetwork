import pandas as pd
import numpy as np

# 如果数据中存在特殊字符检测不出来 isnul sum()
# 使用values_count() 来统计该列元素个数 各个元素出现的次数
# 如果是类别型，非数值型数据存在特殊字符 --可以使用分组聚合，组里会出现特殊字符

# 如果发现特殊字符之后

# 先将特殊字符替换为可以处理的NaN字符

# 加载数据
data = pd.read_excel('./qs.xlsx')

print('data:\n', data)

# 按照门店编号分组，看 商品ID， 出现次数

res = data.groupby(by='门店编号')['商品ID'].count()
print('res:\n', res)

# 转换特殊字符
# replace
# 参数1 特殊字符
# 参数2 np.nan
# inplace = True
data.replace('*', np.nan, inplace=True)

# 检测
res = pd.isnull(data).sum()
print('检测结果:\n', res)


# 删除填充 插值 看具体情况
print()