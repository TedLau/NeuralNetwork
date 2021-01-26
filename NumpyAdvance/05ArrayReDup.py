import numpy as np

# 数组去重  unique函数  并排序 编码排序 unicode ascii

# 创建数组

arr = np.array([2, 2, 2, 2, 2, 1, 1, 2, 21, 23, 12, 1, 23, 1, 23, 12, 3, 123, 12, ])
res = np.unique(arr)
print(arr)
# [  2   2   2   2   2   1   1   2  21  23  12   1  23   1  23  12   3 123
#   12]
print('*' * 100)
print(res)
# [  1   2   3  12  21  23 123]
