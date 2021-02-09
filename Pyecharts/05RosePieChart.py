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

pie = Pie(  # 类型初始化
    init_opts=opts.InitOpts(bg_color='#F0E68C',
                            theme=ThemeType.DARK)

)

# 增加数据
## 对pie进行数据增加
pie.add(
    series_name='分校人数',
    data_pair=data.values.tolist(),
    radius=['50%', '70%'],
    rosetype='radius'  # 玫瑰图绘制
)

# 增加全局配置
pie.set_global_opts(
    title_opts=opts.TitleOpts(title='Python地区分校占比图.html',
                              pos_left='center'),
    legend_opts=opts.LegendOpts(is_show=False)
)

# 增加系列配置
# formatter 显示格式
pie.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True, color='red', font_size=14,
                              formatter='{b}:{d}',  # {b} 代表数据线名称, {c}数据线的值 {d}数据项所占比例
                              )
)

pie.render('./ROSEChart.html')
