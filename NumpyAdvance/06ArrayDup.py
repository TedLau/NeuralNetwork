import numpy as np

# np.tile repeat

arr = np.array([[1, 2, 3], [3, 2, 4], [1, 2, 4]])
print(arr)
# [[1 2 3]
#  [3 2 4]
#  [1 2 4]]
print('*' * 100)
res = np.tile(arr, 2)  # 默认列的方向复制两次
# [[1 2 3 1 2 3]
#  [3 2 4 3 2 4]
#  [1 2 4 1 2 4]]
# np.tile(arr,[2,2,2]) 在列在行在块上各重复两次

print(res)

# args: 1 重复的数组 2 重复的次数 axis重复的方向 不指定轴会展开，在列方向上以每个元素进行重复
print('*' * 100)
res = np.repeat(arr, 2, axis=1)
print(res)
# [[1 1 2 2 3 3]
#  [3 3 2 2 4 4]
#  [1 1 2 2 4 4]]