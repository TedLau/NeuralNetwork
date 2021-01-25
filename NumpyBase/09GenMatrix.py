import numpy as np

# mat matrix asmatrix
m1 = np.mat('1 2;3 4')
print(m1)
print(type(m1))  # <class 'numpy.matrix'>

# bmat数组组合成矩阵  可以单独一个参数转为矩阵

arr1 = np.array([[1, 2], [2, 3]])
arr2 = np.arange(4).reshape((2, 2))
print(arr1)
print(arr2)

res = np.bmat('arr1 arr2; arr2 arr2') #不能使用 1 2 3;4 5 6
print(res)
