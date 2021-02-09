# 导入配置项
from pyecharts import options as opts

# 导入柱状图的绘制API
from pyecharts.charts import Bar

# 导入theme
from pyecharts.globals import ThemeType

# 定义一个bar_chart
def bar_chart() -> Bar:
    """
    柱状图绘制
    实例化之后就进行配置
    :return:
    """
    c = Bar(init_opts=opts.InitOpts(page_title='66666',theme=ThemeType.CHALK)
            ) \
        .add_xaxis(xaxis_data=['衬衫', '毛衣', '风衣']) \
        .add_yaxis(series_name='商家A',  # 一类柱子的名称
                   yaxis_data=[112, 113, 124]).add_yaxis(
        series_name='商家B',
        yaxis_data=[24.412, 123]
    ).reversal_axis(). \
        set_global_opts(
        title_opts=opts.TitleOpts(title='Bar——Chart', title_link='www.guoyashuai.top', title_target='guoyashuai.top'),

    ). \
        set_series_opts(
        label_opts=opts.LabelOpts(position='right')  # 设置数字的显示位置
    )
    # 旋转方向

    return c


bar_chart().render('./BarC.html')
