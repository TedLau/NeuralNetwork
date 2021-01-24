import numpy as np

# arr = np.arange(1, 12, 3)
# print(arr)
#
# print("维度:", arr.ndim)
# print("形状:", arr.shape)
# # [ 1  4  7 10]
# # 维度: 1
# # 形状: (4,)
#
# # 下标访问 会降低维度
# print(arr[2])  # 7 # 0 1 2 3 ....
#
# # 切片访问 不包含后者 不降低维度
# print(arr[1:3])  # [4 7] 步长为1省略
#
# print(arr[1:4:2])  # [ 4 10]
#
# # 获取多个元素 使用下标列表
#
# print(arr[[2, -1]])  # [ 7 10]  先获取具体的值，然后组合起来
#
# # 跳过n个，步长n+1


# 创建二维数组

arr = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
print(arr)
print("维度:", arr.ndim)
print("形状:", arr.shape)

# [[1 2 3 4]
#  [4 3 2 1]]
# 维度: 2
# 形状: (2, 4)

print("下标获取第二个2:", arr[1, 2])  # 下标获取第二个2: 2

print("切片获取第二个2:", arr[1:2, 2:3])  # 切片获取第二个2: [[2]]

print("下标切片配合:", arr[1, 2:3])  # 下标切片配合: [2]

print("下标列表获取多个元素:", arr[[1, 1], [2, 3]])  # 下标列表获取多个元素: [2 1]

# 三维 块 行 列


# bool数组索引  只保留对应行为1的 arr[boolA, :] arr[: boolA]只保留列上为1. 都用，则保留交叉值
boolA = np.array([0, 1], dtype=np.bool)
print(boolA)
print("bool数组索引:", arr[boolA, :])

# [False  True]
# bool数组索引: [[4 3 2 1]]
