import numpy as np

# 创建数组

arr = np.arange(16).reshape((4, 4))
print(arr)
print('*' * 100)

# 拆分 hspilt从中间切一刀
res = np.hsplit(arr, 2)
print(res)
# [array([[ 0,  1],
#        [ 4,  5],
#        [ 8,  9],
#        [12, 13]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11],
#        [14, 15]])]

res = np.hsplit(arr, 4)
# [array([[ 0],
#        [ 4],
#        [ 8],
#        [12]]), array([[ 1],
#        [ 5],
#        [ 9],
#        [13]]), array([[ 2],
#        [ 6],
#        [10],
#        [14]]), array([[ 3],
#        [ 7],
#        [11],
#        [15]])]

# spilt axis = 0/1 水平拆分，垂直拆分

# 不均匀拆分
res = np.split(arr, [1, 2], axis=0)  # 三部分 0 1 2-3
print(res)
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]])]
