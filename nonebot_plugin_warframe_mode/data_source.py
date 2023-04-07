#看着更简单
from httpx import AsyncClient

async def get_data_api(url_arg):
    api_url = f'http://nymph.rbq.life:3000/wf/robot/{url_arg}'
    async with AsyncClient() as client:
        r = (await client.get(api_url))
        return r.text

dic = [(
        "所有指令请加上前缀</>"
        '\n一下为warframe指令：'
        '\nwm <搜索词>'
        '\nrm <搜索词>'
        "\nwiki <搜索词>"
        '\n翻译 <搜索词>'
        '\n打折|小小黑|特价'
        '\n新闻| 事件 |警报'
        '\n突击| 裂缝 |入侵'
        '\n奸商| 特价 |地球'
        '\n电波| 仲裁 |扎里曼'
        '\n地球赏金|金星赏金|火卫二赏金'
        '\n火卫二平原|金星平原|地球平原'
    )]

class wfapi():

    #菜单指令
    @classmethod
    async def directives(cls):
        return dic[0]
    # 新闻
    @classmethod
    async def news(cls):
        data = await get_data_api("news")
        return data

    #活动
    @classmethod
    async def events(cls):
        data = await get_data_api("events")
        return data

    #警报
    @classmethod
    async def alerts(cls):
        data = await get_data_api("alerts")
        return data

    #突击
    @classmethod
    async def sortie(cls):
        data = await get_data_api("sortie")
        return data

    #地球赏金
    @classmethod
    async def Ostrons(cls):
        data = await get_data_api("Ostrons")
        return data

    #金星赏金
    @classmethod
    async def Solaris(cls):
        data = await get_data_api("Solaris")
        return data

    #火二赏金
    @classmethod
    async def EntratiSyndicate(cls):
        data = await get_data_api("EntratiSyndicate")
        return data

    #裂缝
    @classmethod
    async def fissures(cls):
        data = await get_data_api("fissures")
        return data

    #打折
    @classmethod
    async def flashSales(cls):
        data = await get_data_api("flashSales")
        return data

    #入侵
    @classmethod
    async def invasions(cls):
        data = await get_data_api("invasions")
        return data

    #奸商
    @classmethod
    async def voidTrader(cls):
        data = await get_data_api("voidTrader")
        return data

    #小小黑
    @classmethod
    async def persistentEnemies(cls):
        data = await get_data_api("persistentEnemies")
        return data

    #地球
    @classmethod
    async def earthCycle(cls):
        data = await get_data_api("earthCycle")
        return data

    #地球平原
    @classmethod
    async def cetusCycle(cls):
        data = await get_data_api("cetusCycle")
        return data

    #舰队
    @classmethod
    async def constructionProgress(cls):
        data = await get_data_api("constructionProgress")
        return data

    #金星平原
    @classmethod
    async def vallisCycle(cls):
        data = await get_data_api("vallisCycle")
        return data

    #电波
    @classmethod
    async def nightwave(cls):
        data = await get_data_api("nightwave")
        return data

    #仲裁
    @classmethod
    async def arbitration(cls):
        data = await get_data_api("arbitration")
        return data

    #火二平原
    @classmethod
    async def cambionCycle(cls):
        data = await get_data_api("cambionCycle")
        return data

    #扎里曼
    @classmethod
    async def zarimanCycle(cls):
        data = await get_data_api("zarimanCycle")
        return data

    #特价
    @classmethod
    async def dailyDeals(cls):
        data = await get_data_api("dailyDeals")
        return data