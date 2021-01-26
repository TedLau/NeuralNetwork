import numpy as np

# arr = np.array([5,4,3,2,6])
# print('arr:\n',arr)

# 对数组使用快排，对不同列的方向(同一行内部)的数据进行排序，对原数组产生影响

# 直接排序

# arr.sort()
# # 升序排序
# print(arr)
# [2 3 4 5 6]

arr = np.array([[2,1,3],[3,2,5],[5,4,6]])
print(arr)
# [[2 1 3]
#  [3 2 5]
#  [5 4 6]]
arr.sort()
print(arr)
# [[1 2 3]
#  [2 3 5]
#  [4 5 6]]


# 间接排序
arr = np.array([4,3,5,1,4,5,6])
print('arr:\n',arr)
# [4 3 5 1 4 5 6]
#  1 3 4 4 5 5 6
# [3 1 0 4 2 5 6]
# 返回的是排序后原来数组中的下标
res = np.argsort(arr)
print(res)
# [3 1 0 4 2 5 6]

# 二维数组也是返回下标 axis 0行内 1列内