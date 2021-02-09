import pandas as pd

# 导入地图模块
from pyecharts.charts import Map

# 导入配置模块
from pyecharts import options as opts

# 导入主体模块
from pyecharts.globals import ThemeType

# 加载数据
data = pd.read_excel('./截至2月17日22时37分疫情数据.xlsx')
print('data:\n', data)

# 各个省里面的数据

# 获取各个省份的数据
# 1、判断省份的数据
bool_mask = data.loc[:, '城市'] == data.loc[:, '省份']
# 2、筛选各个数据
prov_data = data.loc[bool_mask, :]
# 3、设置数据为data_pair
data_pair_data = prov_data.loc[:, ['省份', '确诊数']].values.tolist()
print('data_pair:\n', data_pair_data)

# 绘制中国地图  --Map
# 1、实例化对象
map = Map(
    init_opts=opts.InitOpts(
        width='1200px',
        height='650px',
        theme=ThemeType.PURPLE_PASSION,
    )
)

# 2、增加数据
map.add(
    series_name='中国早期疫情数据',
    data_pair=data_pair_data,
    maptype='china',
)

# 3、添加全局配置
map.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='早期疫情地图',
        subtitle='郑州大学信息工程学院',
        pos_left='3%',
        pos_top='3%',
    ),
    # 视觉配置选项
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,  # 开启视觉配置
        type_='color',
        is_piecewise=True,
        pieces=[
            {"min": 10001, "label": ">10000", "color": "#4b0101"},
            {"max": 10000, "min": 5001, "label": ">5000", "color": "#4a0100"},
            {"max": 5000, "min": 1001, "label": ">1000", "color": "#8A0808"},
            {"max": 1000, "min": 500, "label": "500-1000", "color": "#B40404"},
            {"max": 499, "min": 100, "label": "100-499", "color": "#DF0101"},
            {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
        ]

    ),
    # 添加图例配置
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_top='3%'
    )
)

# 生成
map.render('./中国早期疫情地图.html')
