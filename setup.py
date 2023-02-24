# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name = "nonebot_plugin_warframe_mode", ##模块名字
    version = "0.0.1", ##版本号
    author="mmxd12", ##作者名字
    author_email="mys0627@outlook.com", ##作者邮箱
    description="""基于nonebot2的WM市场查询的插件""", ##模块简介
    url="https://github.com/mmxd12/nonebot_plugin_warframe_mode", ##模块链接
    py_modules=['nonebot_plugin_warframe_mode.data_source']
)