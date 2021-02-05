import os

def remove_ad_text(dir2, ad_text):
    """用来实现删除特定广告文本的函数。

    该函数会搜索检查指定根目录下的所有文件以及子目录，如果子目录下依然
    存在子目录，则会一直查找下去，直到没有子目录为止。然后将目录名与文件
    名中含有的广告词进行删除。

    Parameters:
    -----
    dir2 : str
        指定要检查的根目录。
    ad_text : str
        指定要删除的广告词。
    """

    #  如果dir2表示的不是一个目录，则直接返回。
    if not os.path.isdir(dir2):
        return
    # 如果传递的dir2末尾没有路径分隔符，我们就加入路径分隔符。
    if not dir2.endswith(os.path.sep):
        dir2 += os.path.sep

    # 获取目录下所有的子目录以及文件名。(返回列表类型)
    names = os.listdir(dir2)
    # 依次遍历每一个子目录或文件名。（对子目录与文件的处理方式是不同的。）
    for name in names:
        # 拼接成完整的路径。（包含路径与文件名。）
        sub_path = os.path.join(dir2, name)
        # 判断该路径表示的是否为目录
        if os.path.isdir(sub_path):
            # 如果是目录，则要进行递归的判断查找（下钻）
            remove_ad_text(sub_path, ad_text)
        # 将当前文件（目录）进行重命名，去掉广告词。
        name = name.replace(ad_text, "")
        # 组合新的路径
        new_path = os.path.join(dir2, name)
        # 对文件（目录）名进行重命名。
        os.rename(sub_path, new_path)
remove_ad_text('E:\\视频资料\神经网络\\','【瑞客论坛 www.ruike1.com】')
