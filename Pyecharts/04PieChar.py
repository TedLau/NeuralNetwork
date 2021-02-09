# 导入配置项
from pyecharts import options as opts

# 导入模块
from pyecharts.charts import Pie
# 导入theme
from pyecharts.globals import ThemeType

import pandas as pd

# 加载数据

data = pd.read_excel('./Python地区分校人数.xlsx')
print('data:\n', data)

# 绘制饼图
pie = Pie(

)
pie.add(
    series_name='分校人数',
    data_pair=data.values.tolist(),  #
    radius=[
        '50%', '75%'  # 内外半径 内径 外径
    ]
)

# 添加全局配置
pie.set_global_opts(
    title_opts=opts.TitleOpts(title='分校占比图',
                              pos_left='center'),
    legend_opts=opts.LegendOpts(is_show=False),
)

# 添加系列配置
pie.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True,
                              color='#8FBC8F',
                              font_size=15, )
)

# 实例化生成
pie.render('./Python系统班地区占比图.html')
