import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name = "nonebot_plugin_warframe_mode", ##模块名字
    version = "0.0.4", ##版本号
    author="mmxd12", ##作者名字
    author_email="mys0627@outlook.com", ##作者邮箱
    description="""基于nonebot2的WM市场查询的插件""", ##模块简介
    long_description=long_description,  # 加长版描述？
    long_description_content_type="text/markdown",  # 描述使用Markdown
    url="https://github.com/mmxd12/nonebot_plugin_warframe_mode", ##模块链接
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.11",  # 使用Python3.11,建议使用3.9以上
        "License :: OSI Approved :: MIT License",  # 开源协议
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.2.1',
        'httpx>=0.23.3',
    ],
)