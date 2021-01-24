#  numpy 封装了Python中的数据类型 细致的划分
import numpy as np

#  创建数组可以使用dtype参数指定

# arr = np.array([1, 23.4], dtype=np.float64)
# print(arr.size)
# print(type(arr))
# print(arr.dtype)

#  强制转化  --most used
# print(np.float(32))
# print(np.int(3.12))
###

#  不推荐使用自定义复合类型
# df = np.dtype([('name', np.str, 40), ('height', np.float64), ('weight', np.float64)])
# arr = np.array([('zs', 180, 75), ('ls', 190, 89)], dtype=df)
# print(arr)
