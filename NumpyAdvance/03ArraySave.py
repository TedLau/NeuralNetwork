import numpy as np

# 以二进制形式保存
arr = np.arange(16).reshape((4, 4))
print(arr)

# 保存 save  单个数组
# args: 1：路径+名称，后缀省略默认为.npy的二进制文件
#       2：需要保存的数组
np.save('./arr1', arr)

# 使用.npy文件
# 参数 路径+名称 需要加后缀 load
# data = np.load('./arr1.npy')
# print(data)

# 保存多个数组 savez
# args: 1：路径+名称  默认后缀为npz
#       2：需要保存的数组，之间用,分隔开
arr2 = np.array([1, 2, 3])
np.savez('./arr1', arr, arr2)

# 打印已保存的数组
res = np.load('./arr1.npz')
print(res)  # <numpy.lib.npyio.NpzFile object at 0x000001D4FDE0C070>
# 保存以key:value保存
# 遍历
for i in res:
    print(i)

# arr_0
# arr_1
# 则可以以用键寻值的方式来识别
x = res['arr_0']
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
y = res['arr_1']
# [1 2 3]
print(x)
print(y)

# 给数组指定的键 前面的是key  后面的是变量名
np.savez('./arr1', arr=arr, arr2=arr2)

# 加载指定key 的.npz文件

res = np.load('arr1.npz')
print(res['arr'])

# 数组以文本形式保存

arr = np.arange(16).reshape((4, 4))
print(arr)

# args: 1:文件路径+名称 .txt csv ----->序列化的文本文件
#       2:需要保存的数组
#       fmt--保存的格式 默认科学计数法
#       分隔符     默认空格分隔

# np.savetxt('./arr.txt', arr, fmt="%d", delimiter=',')

# 不可以读取缺失数据的文本 加载文本，需要指定分隔符，否则会引起报错，dtype是指定加载出来的元素的类型
# res = np.loadtxt('./arr.txt', dtype=float, delimiter=',')
# print(res)

# genfromtxt可以加载缺失数据
data = np.genfromtxt('./arr.txt', dtype=int, delimiter=',')
