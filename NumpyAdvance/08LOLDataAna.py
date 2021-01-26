import numpy as np

res = np.load('./lol_data.npz')
for i in res:
    print(i)
# columns
# data

columns = res['columns']
data = res['data']
print('columns:\n', columns)
print('data:\n', data)


# 按照行方向去重 即为行增加的方向
data = np.unique(data,axis=0)
print(data)
# 获取平均薪资
salary = data[:, 4]  # 对列操作
# 修改类型
salary = salary.astype('float')
print('salary mean:\n', np.mean(salary))
