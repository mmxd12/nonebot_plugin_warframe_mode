# nonebot-plugin-warframe_mode

基于NoneBot2的WM市场查询的插件
- 关于插件更新！
  
    ```shell
    1.最新版插件未上转pypi，建议直接clone本库，然后开发者模式下使用
    2.如有新版，一样会上到本库
    ...
    ```


# 安装

- NoneBot2 插件商店安装

    ```shell
    nb plugin install nonebot-plugin-warframe_mode
    ```

- 手动安装

    ```shell
    pip install nonebot-plugin-warframe_mode
    ```
	
- 打开nonebot2的根目录中的pyproject.toml文件，在[tool.nonebot]这项中找到plugins在其后面[]里写入"nonebot_plugin_warframe_mode"。**此办法插件可能不是最新版！建议clone本库，然后在开发者模式下使用**

# 使用

- 前缀：`/`
- 指令菜单：`救命 菜单`
  ```text
  注意：所有指令需要搭配前缀使用！
  指令参数：
  ==================
  wm <搜索词>
  rm <搜索词>
  wr/zk <搜索词>
  wmw/xh/玄骸 <搜索词>
  wiki <搜索词>
  翻译 <搜索词>
  打折|小小黑|特价
  新闻| 事件 |警报
  突击| 裂缝 |入侵
  奸商| 特价 |地球
  电波| 仲裁 |扎里曼
  地球赏金|金星赏金|火卫二赏金
  火卫二平原|金星平原|地球平原
  ===================
  当前版本1.1.1-Beta
  ```
  
# 注意

python版本需要3.9以上，内置新语法！
如果有bug请大佬们往[issues]走(https://github.com/mmxd12/nonebot_plugin_warframe_mode/issues)
如需修改指令前缀或者监听的ip请在.env文件里面修改！
pillow库请使用9.5.0版:`pip install pillow==9.5.0`
如有其他疑问可如群:435021808 感谢你的使用！


# 特别感谢

- [NoneBot2](https://github.com/nonebot/nonebot2)： 插件使用的开发框架。
- [LLOneBotDoc](https://github.com/LLOneBot/LLOneBotDoc)：推荐使用LLOneBotDoc目前最合适小白使用的野生！！！
- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)： 无理头●▽●。（虽然已寄但可以使用Gensokyo给官方bot使用[Gensokyo](https://github.com/Hoshinonyaruko/Gensokyo)）
- [warframe-info-api](https://github.com/WsureWarframe/warframe-info-api)：所使用的指令均来自WsureWarframe的api（非常的nbヾ(≧∇≦*)ゝ）
