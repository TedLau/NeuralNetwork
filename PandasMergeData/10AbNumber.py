import pandas as pd
import numpy as np


# 异常值
# 明显偏离正常值的值，直接删除
# 判断异常值
# 1、具体业务法
# 2、3sigma原则  均值+- 三倍的标准差
# 3、箱线分析法
# qu 上四分位数 0.75位置处的值
# ql下四分位数 0.25位置处的数值
# iqr 四分位间距 (qu-ql)
# 　数值处于　(ql - 1.5*iqr,qu+1.5*iqr) 这之间的数据认为是正常的数据

def just_h(data):
    bool_mask = (data < 230) & (data > 30)
    return bool_mask



# 判定身高
# 自定义判断身高的函数 数值异常的删除

height = pd.Series(data=[180, 190, 12, 150, 200],
                   index=['stu_0', 'stu_1', 'stu_2', 'stu_3', 'stu_4'])

print('height:\n', height)
# 返回一个bool数组
bool_mask = just_h(height)
print('之后的数据:\n', height[bool_mask])
