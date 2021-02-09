import pandas as pd

# 导入地图模块
from pyecharts.charts import Map

# 导入配置模块
from pyecharts import options as opts

# 导入主体模块
from pyecharts.globals import ThemeType

# 导入翻译模块
from translate import Translator


# 将中文转为英文

def trans(data):
    """
    中文转英文
    :param data:
    :return:
    """
    tran = Translator(from_lang='chinese', to_lang='english')
    # 转化
    new_data = tran.translate(data)

    return new_data


# 加载数据
data = pd.read_excel('./截至2月17日22时37分疫情数据.xlsx')

print('data:\n', data)
print('*' * 100)

# 获取世界各个国家的疫情数据

bool_mask = data.loc[:, '省份'].str.contains('洲')

country_data = data.loc[bool_mask, :]
print('所有国家的数据:\n', country_data)

# 获取各个的确诊数
country_data = country_data.loc[:, ['城市', '确诊数']]

# 对城市进行转化 使用transform
country_data.loc[:, '城市'] = country_data.loc[:, '城市'].transform(trans)

# 获取pair——data

data_pair_data = country_data.values.tolist()
print('data_pair_data:\n', data_pair_data)

# 1、绘制地图 实例化对象
map = Map(
    init_opts=opts.InitOpts(
        width='1200px',

    )
)

# 2、添加数据
map.add(
    series_name='截至2020.2.17的疫情数据',
    data_pair=data_pair_data,
    maptype='world',
    is_roam=True,  # 鼠标缩放 和 平移漫游
    is_map_symbol_show=False,  # 关闭地图上的点
)

# 3、添加全局配置
map.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(
        title='2020年早期疫情数据',
        subtitle='郑州大学信息工程学院TedLau',
        pos_left='3%',
        pos_top='3%',
    ),
    # 图例
    legend_opts=opts.LegendOpts(
        is_show=True,
        pos_top='3%',
    ),
    # 视觉配置
    visualmap_opts=opts.VisualMapOpts(
        is_show=True,
        type_='color',
        is_piecewise=True,
        # 指定各个区间内的取值范围、label、颜色
        pieces=[
            {"min": 10001, "label": ">9999", "color": "#4b0101"},
            {"max": 10000, "min": 100, "label": ">99", "color": "#4a0100"},
            {"max": 99, "min": 40, "label": "40-99", "color": "#8A0808"},
            {"max": 39, "min": 30, "label": "30-39", "color": "#B40404"},
            {"max": 29, "min": 20, "label": "20-29", "color": "#DF0101"},
            {"max": 19, "min": 10, "label": "10-19", "color": "#F78181"},
            {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
            {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
        ]
    ),

)

# 添加系列配置
map.set_series_opts(
    label_opts=opts.LabelOpts(
        is_show=False,  # 去掉国家名称
    )
)

# 生成
map.render('./世界早期疫情数据.html')
