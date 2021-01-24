# 科学计算库 -- 多维数据

# 使用 ndarray 对象来存储数据

# ndarray 内存连续的、存储单一数据类型的、多维的数据的 对象

# 两种存储风格，C 行优先（默认） Fortran 列优先

import numpy as np

arr = np.array([1, 2, 4, 5, 6])
print(arr)
print(type(arr))
