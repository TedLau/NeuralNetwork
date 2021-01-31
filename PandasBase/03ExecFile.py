import pandas as pd

# excel csv html json 文件

# read csv read table

# 读取csv文件

info = pd.read_csv(filepath_or_buffer='./meal_order_info.csv',
                   encoding='ansi',
                   header='infer',  # 读取文件时列自动识别，也可以显示指定的，默认为0
                   # names=  自定义显示名称
                   # usecols 指定读取的列下标
                   # index_col 指定特定列为行索引
                   # nrows 指定读取前n行
                   )
print(info)

# read _csv read table 区别在于没有默认的分隔符  可以保存为文件

# 保存文件
# 格式： df.to_xxx格式
# csv保存
info.to_csv(path_or_buf='./aaa.csv',  # 路径 名称
            header=True,  # 需要保存列索引 index 需要保存行索引
            # columns 指定要保存的列
            # mode w 之前写的都会被清除 改为 a 如同C语言
            )
# excel文件 ---以.xlsx .xls为结尾的表格数据文件
detail = pd.read_excel(io='./meal_order_detail.xlsx',  # 文件路径 + 名称
                       sheet_name=None,  # 读取表格下标
                       # header=0,  # 以表格的第0行为列索引
                       # # index_col=0 ,# 可以指定特定列为行索引
                       # parse_cols=[0, 1],  # 读取指定的列
                       )
print('detail:\n', detail)  # --->OrderedDict

# 可以通过
print(detail.keys())  # odict_keys(['meal_order_detail1', 'meal_order_detail2', 'meal_order_detail3'])
print('*' * 100)
# 获取不同的sheet
detail_1 = detail['meal_order_detail1']
detail_2 = detail['meal_order_detail2']
detail_3 = detail['meal_order_detail3']
print('detail_1:\n', detail_1)

# 一次只能保存一个文件里 多次会覆盖
# detail.to_excel(excel_writer='./aaa.xlsx',
#                 sheet_name='Sheet1',
#
#                 header=True,
#                 index=True,)
writer = pd.ExcelWriter('./ccc.xlsx')
# 将不同df 保存到不同sheet中
# 写入数据
detail_1.to_excel(excel_writer=writer, sheet_name='sheet1')
detail_2.to_excel(excel_writer=writer, sheet_name='sheet2')
detail_3.to_excel(excel_writer=writer, sheet_name='sheet3')
# 保存修改
writer.save()
# 关闭ExcelWriter对象
writer.close()