import numpy as np

# 创建数组
arr = np.arange(16)
print(arr)
print("维度:", arr.ndim)
print("arr的形状:", arr.shape)

# 形状的更改  由于部分时候不易于计算，
arr.shape = (4, 4)
print(arr)

# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
# 维度: 1
# arr的形状: (16,)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# reshape需要数组来接收

# 使用np.arange & reshape 可以得到高维度数组  元素个数不变

# 同时使用np.arange & reshape
# arr = np.arange(16).reshape((2, 8))
# print(arr)
# [[ 0  1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14 15]]

# arr = np.arange(16).reshape((2, 2, 2, 2))
# print(arr)
# [[[[ 0  1]
#    [ 2  3]]
#   [[ 4  5]
#    [ 6  7]]]
#  [[[ 8  9]
#    [10 11]]
#   [[12 13]
#    [14 15]]]]

# arr = np.arange(16).reshape((8, 2))
# print(arr)
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]
#  [12 13]
#  [14 15]]

arr = np.arange(15).reshape((3, 5))
print(arr)

# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]

# 展开为一维数组 flatten 返回一个拷贝 ravel: 返回自己的视图，相当于是一个地址，修改会改变原来的值
new_arr = arr.flatten()
print(new_arr)
arr.ravel()
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
# ravel 参数 F会按照列展开

print(arr.reshape((-1,)))
# 负数是占位作用，不可以用正数 不管多少列，只管在一行展开 -1 1则表示不管多少行，每列只有一个数据
