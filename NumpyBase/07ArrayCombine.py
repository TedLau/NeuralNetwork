import numpy as np

# 创建数组
arr1 = np.arange(4).reshape((2, 2))
arr2 = np.array([[0, 1], [2, 1]])
print("1:", arr1)
print("2:", arr2)

# 合并
# 向下拼接 ----垂直拼接
print(np.vstack((arr1, arr2)))
# param tuple
# [[0 1]
#  [2 3]
#  [0 1]
#  [2 1]]
# [[0 1 0 1]
#  [2 3 2 1]]


# 向右拼接 ----水平拼接
print(np.hstack((arr1, arr2)))  # 引申 水平拆分
# [[0 1]
#  [2 3]
#  [0 1]
#  [2 1]]
# [[0 1 0 1]
#  [2 3 2 1]]

# concatenate a1,a2 axis: int  (0) (0,1) == (行,列)
print(np.concatenate)
