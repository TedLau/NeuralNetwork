import numpy as np

# 创建矩阵
m1 = np.mat('1 2;3 4')
m2 = np.mat([[1, 2], [3, 2]])
print('m1:', m1)
print('m2:', m2)

print('*' * 100)
print(m1 + m2)

print('*' * 100)
print(m1 * 4)

print('*' * 100)
print("矩阵相乘:", np.matmul(m1, m2))
print('*' * 100)
# 矩阵相乘: [[ 7  6]
#  [15 14]]
print("矩阵相乘:", np.dot(m1, m2))
# 矩阵相乘: [[ 7  6]
#  [15 14]]

print('*' * 100)
print("矩阵对应元素相乘:", np.multiply(m1, m2))

# 矩阵的转置
print('m1的转置:', m1.T)
# m1的转置: [[1 3]
#  [2 4]]
# 矩阵的逆
print('m1的逆矩阵:', m1.I)

# inf 无穷
# m1的逆矩阵: [[-2.   1. ]
#  [ 1.5 -0.5]]

# 矩阵的视图
# 可以通过.A将矩阵转为ndarray  使用下标会降低维度
# 可以通过np.mat将ndarray转为矩阵 
print('m1的视图:', m1.A)


