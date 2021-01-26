import numpy as np

# sum
# mean
# std(标准差)
# var 方差
# min
# max
# argmax (最大值的下标)
# argmin (最小值的下标)
# cumsum (累积和)
# cumprod (累计积)

arr = np.arange(1, 17).reshape((4, 4))
print('arr:\n', arr)

# np numpy里的方法
# arr ndarray列队方法


print('累积和:\n', np.cumsum(arr, axis=0))  # 不指定轴 展开进行运算 1:行内累加 0:列内累加
print('累计积:\n', np.cumprod(arr))
