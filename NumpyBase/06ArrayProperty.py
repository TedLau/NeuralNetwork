import numpy as np
# 0 维 单独的数字 4维 堆 块 行 列
# np.array 创建数组

# ndip shape size dtype itemsize
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr)
# print(type(arr))  # <class 'numpy.ndarray'>
#
# print("Size(cnt):", arr.size)
# print('Elem size:', arr.itemsize)  # 4字节
# print('Elem Type:', arr.dtype)  # int32
#
#
# print('Arr shape:', arr.shape)  # (6,) -->元组 列维度的数量
# print('Arr dim:', arr.ndim)  # 1维 -->列维度


# arr = np.array([[1, 2, 3, 4, 6], [5, 6, 7, 8, 10], [1, 2, 3, 4, 5]])
# print(arr)
# print(type(arr))  # <class 'numpy.ndarray'>
# print("Size(cnt):", arr.size)
# print('Elem size:', arr.itemsize)  # 4字节
# print('Elem Type:', arr.dtype)  # int32
#
#
# print('Arr shape:', arr.shape)  # (2,4) -->元组 列维度的数量
# print('Arr dim:', arr.ndim)  # 2维 -->列+行维度


arr = np.array([[[1, 2, 3, 4, 6], [5, 6, 7, 8, 10]], [[1, 2, 3, 4, 6], [5, 6, 7, 8, 10]], [[1, 2, 3, 4, 6], [5, 6, 7, 8, 10]]])

print(arr)
print(type(arr))  # <class 'numpy.ndarray'>
print("Size(cnt):", arr.size)
print('Elem size:', arr.itemsize)  # 4字节
print('Elem Type:', arr.dtype)  # int32


print('Arr shape:', arr.shape)  # (3,2,5) -->元组 列维度的数量

# [[[ 1  2  3  4  6]
#   [ 5  6  7  8 10]]

#  [[ 1  2  3  4  6]
#   [ 5  6  7  8 10]]

#  [[ 1  2  3  4  6]
#   [ 5  6  7  8 10]]]
print('Arr dim:', arr.ndim)  # 3维 -->块+行+列维度
