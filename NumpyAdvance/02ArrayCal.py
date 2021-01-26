import numpy as np

# 数组全通函数  --可以对数组中所有元素进行操作的函数  以整个函数为输出
# 运算的数组必须是同型
arr1 = np.array([[1, 2], [2, 3]])
arr2 = np.arange(2, 6).reshape((2, 2))
print("arr1:", arr1)
print("arr2:", arr2)
# （1）四则运算
print('*' * 100)
print("plus:", arr1 + arr2)
print('*' * 100)
print('minus:', arr1 - arr2)
print('*' * 100)
print('mul:', arr1 * arr2)
print('*' * 100)

# （2）比较运算 > < >= <= == !=  返回bool数组
print('==:', arr1 == arr2)
print('*' * 100)
# ==: [[False False]
#  [False False]]


# （3）逻辑运算  具体bool值
# np.all全部满足才为true np.any有满足则不为false
print("==:", np.all(arr1 == arr2))

# 先比较==再根据运算结果进行索引
height = np.array([11, 12, 13, 14, 155])
print(height)
# [ 11  12  13  14 155]
bool_mask = height % 2 == 0
print(bool_mask)
# [False  True False  True False]
new_height = height[bool_mask]
print(new_height)
# [12 14]

# ==: False

# 数组广播机制 --不同型的数组的运算规则
# 1：让所有输入的数组都向其中shape最长的数组看齐 shape不足的部分通过在前面补1补齐
# 2：输出数组的shape是输入数组shape各个轴上的最大值
# 3：如果输入数组的某个轴和输出数组的对应长度相同或者其长度为1时，这个数组能够用来计算，否则出错
# 4：挡输入数组的某个轴的长度为1时，沿着此轴运算时都用此轴上的第一组值。

# arr1 shape(1,2,3,4,,4,5,6)
# arr2 shape(1,2,4,4,1,1) 前面补1，则为(1,1,2,4,4,1,1)
#     (1,1,2,4,4,1,1)
#     (1,2,3,4,4,5,6)
#          2,3不相等且没有一个为1的。
