# 如果存在单列多列中国数据一样
# 则该数据无法使用，无效
# 删掉 drop函数
# 如何判定整列数据一致？
# 1、Python自定义函数统计
# 2、set 进行去重
# 3、drop_duplicate去重


# ndarray中unique去重
# subset去重的列
# keep=’first‘ 保存第一次出现的数据

# 特征重复：bool数组判断是否相同
# 如果存在大量数据都一样，可以利用相似度、相关性系数来衡量

import pandas as pd

# 加载detail数据

detail = pd.read_excel('./meal_order_detail.xlsx')

# 计算 amounts counts的相关性计算
# 默认皮尔逊相关系数
print('两列之间的相关性计算:\n', detail.loc[:, ['amounts', 'counts']].corr())

# 两列之间的相关性计算:
#            amounts    counts
# amounts  1.000000 -0.174648
# counts  -0.174648  1.000000

# 呈现负相关 相关性系数较小。
