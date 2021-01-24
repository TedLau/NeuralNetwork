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

