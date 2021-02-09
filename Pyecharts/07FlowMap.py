# 导入绘制流向地图模块
from pyecharts.charts import Geo
# 导入配置模块
from pyecharts import options as opts
# 导入主体配置模块，GeoType模块
from pyecharts.globals import ThemeType, GeoType, SymbolType

# 绘制流向地图
# 基于早期数据

# 出--代表从武汉--->该城市
# 入--代表从该城市--->武汉
data_0120_ru = '孝感、黄冈、鄂州、荆州、黄石、襄阳'
data_0120_chu = '孝感、黄冈、荆州、襄阳、黄石、荆门、鄂州、随州、仙桃'
data_0121_ru = '孝感、黄冈、荆州、鄂州、黄石'
data_0121_chu = '孝感、黄冈、荆州、襄阳、荆门、黄石、随州、鄂州、仙桃'
data_0122_ru = '孝感、黄冈、鄂州、荆州、咸宁、黄石'
data_0122_chu = '孝感、黄冈、荆州、襄阳、荆州、随州、宜昌、黄石、鄂州'

# 修改数据 data_pair 要求的形式
# [a,b]
# 构建入武汉
data_in = [data_0120_ru, data_0121_ru, data_0122_ru]
# 构建出武汉
data_out = [data_0120_chu, data_0121_chu, data_0122_chu]

# 构建迁移路线　－－ｌｉｓｔ
data_move = []

for i in data_in:
    # 对数据继续拆分
    data_city_in = i.split('、')
    print('data_city_in:\n', data_city_in)
    for city in data_city_in:
        # 构建迁移路线
        data_move.append([city, '武汉'])

for i in data_out:
    # 对数据继续拆分
    data_city_out = i.split('、')
    print('data_city_in:\n', data_city_out)
    for city in data_city_out:
        # 构建迁移路线
        data_move.append(['武汉', city])

# 1、实例化Geo对象
geo = Geo(
    init_opts=opts.InitOpts(
        width='1200px',  # 宽高地图
        height='1000px',
        page_title='武汉封城人员流向地图',
        bg_color='#1f3b4d',
        theme=ThemeType.CHALK,
    )
)

# 2、添加配置
geo.add_schema(
    # maptype China 中国地图
    # world  世界地图
    maptype='湖北',
    itemstyle_opts=opts.ItemStyleOpts(
        color='blue',
        border_color='#ffdf22',
    )
)

# 3、添加数据

geo.add(
    series_name='',
    data_pair=data_move,
    type_=GeoType.LINES,
    # 点的样式
    effect_opts=opts.EffectOpts(
        # 点的样式 为箭头样式
        symbol=SymbolType.ARROW,
        # 点的大小
        symbol_size=6,
        # 点的颜色
        color='yellow'
    ),
    # 线的样式
    linestyle_opts=opts.LineStyleOpts(
        # width 宽度
        curve=0.2,
    ),

    # 标签样式
    label_opts=opts.LabelOpts(
        is_show=True
    ),
    # 是否启用大规模线图的优化  数据特别多可以开启
    is_large=True
)

# 设置标题
# 全局配置  -title
# 全局配置文本
geo.render('./WHFCQRYQXT.html')
