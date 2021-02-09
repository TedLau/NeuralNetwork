# 导入配置项
from pyecharts import options as opts

# 导入模块
from pyecharts.charts import Bar, Line, Grid
# 导入theme
from pyecharts.globals import ThemeType

import pandas as pd

# 加载数据
his = pd.read_excel('./疫情历史数据.xls')
print('hist:\n', his)

# 准备横轴数据
# pycechart 不支持 其它类型 int float bool  dict   str  list
# 将时间序列转化为字符串
his.loc[:, '时间'] = his.loc[:, '时间'].astype('str')
time_data = his.loc[:, '时间'][::-1].values.tolist()
print('time_data:\n',
      time_data)

# 纵轴数据准备
# 死亡人数
death_num = his.loc[:, '死亡数'][::-1].values.tolist()
print('death_num:\n', death_num)
# 确诊人数
diag_num = his.loc[:, '确诊数'][::-1].values.tolist()
print('diag_num:\n', diag_num)
# 治愈人数
cured_num = his.loc[:, '治愈数'][::-1].values.tolist()
print('cured_num:\n', cured_num)
# 疑似人数
suspect_num = his.loc[:, '疑似数'][::-1].values.tolist()
print('suspect_num', suspect_num)

# 使用bar来绘制死亡数和治愈数
# 实例化对象
bar = Bar()

# 添加数据
# 添加横轴数据
bar.add_xaxis(time_data)
# 添加纵轴数据

# 死亡人数
bar.add_yaxis(
    series_name='死亡数',
    yaxis_data=death_num,
    color='red',
    yaxis_index=1,  # 最后多个纵轴时 可以做纵轴的选择
)
# 治愈人数
bar.add_yaxis(
    series_name='治愈数',
    yaxis_index=2,
    yaxis_data=cured_num,
    color='green',
)

# 设置额外的坐标轴
bar.extend_axis(
    # 配置新的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # value 表示数据轴 category 表示类目轴 time 表示时间轴
        name='死亡数',
        is_show=True,  # 展示
        min_=0,
        max_=700,  # 刻度轴的最大值
        position='right',  # 显示位置
        # offset=60,  # 偏离位置

        # 轴线配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示轴线
            # 设置轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='blue'
            )
        ),
        # 设置对应的标签， ｛｝ 数据
        axislabel_opts=opts.LabelOpts(
            formatter='{value}'
        )
    )
)
bar.extend_axis(
    # 配置新的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # value 表示数据轴 category 表示类目轴 time 表示时间轴
        name='治愈数',
        is_show=True,  # 展示
        min_=0,
        max_=1300,  # 刻度轴的最大值
        position='right',  # 显示位置
        offset=60,  # 偏离位置

        # 轴线配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示轴线
            # 设置轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='orange'
            )
        ),
        # 设置对应的标签， ｛｝ 数据
        axislabel_opts=opts.LabelOpts(
            formatter='{value}'
        )
    )
)
bar.extend_axis(
    # 配置新的纵轴
    yaxis=opts.AxisOpts(
        type_='value',  # value 表示数据轴 category 表示类目轴 time 表示时间轴
        name='疑似数',
        is_show=True,  # 展示
        min_=0,
        max_=30000,  # 刻度轴的最大值
        position='right',  # 显示位置
        offset=120,  # 偏离位置

        # 轴线配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,  # 显示轴线
            # 设置轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='gray'
            )
        ),
        # 设置对应的标签， ｛｝ 数据
        axislabel_opts=opts.LabelOpts(
            formatter='{value}'
        )
    )
)
# 设置全局配置

bar.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='中国早期疫情变化趋势图',
        subtitle='郑州大学信息工程学院TedLau',
        subtitle_textstyle_opts=opts.TextStyleOpts(
            font_size=12,
            width='1.6',
        ),
        pos_left='3%',  # title 的位置
        pos_top='1%',

    ),
    # 图例
    legend_opts=opts.LegendOpts(
        pos_left='25%',
        pos_top='7%',
    ),
    # 提示框
    tooltip_opts=opts.TooltipOpts(
        trigger='axis',  # 坐标轴。柱状图
        axis_pointer_type='cross',  # 十字准星指示 表示启用两个正交的轴
    ),
    # 对纵轴的全局配置
    yaxis_opts=opts.AxisOpts(
        type_='value',
        name='确诊数',
        min_=0,
        max_=30000,
        # 轴线的配置
        axisline_opts=opts.AxisLineOpts(
            is_show=True,
            # 轴线风格
            linestyle_opts=opts.LineStyleOpts(
                color='#fd5956'
            )
        ),
        # 轴线对应标签的数据  {value}  数据
        axislabel_opts=opts.LabelOpts(
            formatter='{value}'
        )
    ),

    # 插入文本框
    graphic_opts=opts.GraphicGroup(

        # 图形配置
        graphic_item=opts.GraphicItem(
            # 控制整体的位置
            left='75%',
            top='45%',
        ),
        children=[
            # GraphicRect控制方框的显示
            # opts.GraphicRect(
            #     graphic_item=opts.GraphicItem(
            #         z=100,  # 文本的高度
            #         left='center',
            #         top='middle',
            #     ),
            #     graphic_shape_opts=opts.GraphicShapeOpts(
            #         width=420,  # 宽度
            #         height=180,  # 高度
            #     ),
            #     graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
            #         fill='#fff',  # 文本框填充颜色
            #         stroke='#555',  # 笔画颜色
            #         line_width=2,
            #         shadow_blur=8,
            #         shadow_offset_x=3,
            #         shadow_offset_y=3,
            #         shadow_color='rgba(0,0,0,0.3)',  # 阴影颜色
            #     )
            # ),
            # 配置文本
            opts.GraphicText(
                # 配置文本的位置
                graphic_item=opts.GraphicItem(
                    left='center',
                    top='middle',
                    z=100,
                    scale=[1.5, 1.5]  # 缩放
                ),
                graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                    text="直到{}，\n全国的新冠状肺炎病毒的相关信息为：\n死亡病例为{}例,\n治愈病例为{}例,\n确诊病例为{}例,\n疑似病例为{}例,专家呼吁:\n广大积极配置国家政策进行疫情防疫工作".format(
                        his.loc[0, '时间'],
                        his.loc[0, '死亡数'],
                        his.loc[0, '治愈数'],
                        his.loc[0, '确诊数'],
                        his.loc[0, '疑似数']),
                    font="15px Microsoft YaHei",
                    text_align='left',
                    text_vertical_align='middle',  # 垂直对齐方式　默认Ｎｏｎｅ
                    # 图形配置
                    graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                        fill='#ffdf22',
                        line_width=1.2,
                    )
                )
            )
        ]
    )
)
# 添加系列配置
bar.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True),  # 设置开启label
)

# 绘制折线图
line1 = Line()

# 添加数据
line1.add_xaxis(time_data)
line1.add_yaxis(
    series_name='确诊数',
    y_axis=diag_num,
    color='#4b0101',
    label_opts=opts.LabelOpts(is_show=True),
    linestyle_opts=opts.LineStyleOpts(
        width=1.2,
        color='#4b0101'
    )
)

# 添加其他折线图
line2 = Line()
line2.add_xaxis(time_data)
line2.add_yaxis(
    series_name='疑似数',
    y_axis=suspect_num,
    color='#fed0fc',
    # 标签配置
    label_opts=opts.LabelOpts(is_show=False),
    # 线
    linestyle_opts=opts.LineStyleOpts(
        width=1.2,
        color='#fed0fc'
    )

)

# 合并两个图
sumx = bar.overlap(line1).overlap(line2)

#  组合
all_ = Grid(
    init_opts=opts.InitOpts(
        width='1750px',  # 宽度
        height='654px',  # 高度
        theme=ThemeType.PURPLE_PASSION,
    )
)

all_.add(sumx,
         grid_opts=opts.GridOpts(
             pos_left='5%',
             pos_top='20%',
             pos_right='40%'
         ),
         is_control_axis_index=True,
         )

# 生成
all_.render('./conv-19.html')


# 1、绘制2个柱状图  ---应该添加 3个新纵轴、 修改1个原来的纵轴(全局配置项)
# 2、绘制1个折线图
# 3、再绘制1个折线图
# 4、overlap 组合 ----层叠
# 5、控制 多个图表大小、主题 ---overlap组合多个图表 加入到 Grid组合
# 6、全局配置项里面---配置相关文本