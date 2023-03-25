#主要在这边本来可以用一个列表全卷关键起来然后用网址访问，但为了方便新人观看///其实是直接cai
####建议3.9版本py使用
#如网址为http://nymph.rbq.life:3000/wf/robot/《指令》指令这里可以搞一个列表访问

import httpx
#指令菜单
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
#print(dic[0])

async def directives():
    return dic[0]
#新闻
async def get_news_api():
    news_url = 'http://nymph.rbq.life:3000/wf/robot/news'
    async with httpx.AsyncClient() as client:
        news = await client.get(url=news_url)
        return news.text
#活动
async def get_events_api():
    events_url = 'http://nymph.rbq.life:3000/wf/robot/events'
    async with httpx.AsyncClient() as client:
        events = await client.get(url=events_url)
        return events.text
#警报
async def get_alerts_api():
    alerts_url = 'http://nymph.rbq.life:3000/wf/robot/alerts'
    async with httpx.AsyncClient() as client:
        alerts = await client.get(url=alerts_url)
        return alerts.text
#突击
async def get_sortie_api():
    sortie_url = 'http://nymph.rbq.life:3000/wf/robot/sortie'
    async with httpx.AsyncClient() as client:
        sortie = await client.get(url=sortie_url)
        return sortie.text
#地球赏金
async def get_Ostrons_api():
    Ostrons_url = 'http://nymph.rbq.life:3000/wf/robot/Ostrons'
    async with httpx.AsyncClient() as client:
        Ostrons = await client.get(url=Ostrons_url)
        return Ostrons.text
#金星赏金
async def get_Solaris_api():
    Solaris_url = 'http://nymph.rbq.life:3000/wf/robot/Solaris'
    async with httpx.AsyncClient() as client:
        Solaris = await client.get(url=Solaris_url)
        return Solaris.text
#火二赏金
async def get_EntratiSyndicate_api():
    EntratiSyndicate_url = 'http://nymph.rbq.life:3000/wf/robot/EntratiSyndicate'
    async with httpx.AsyncClient() as client:
        EntratiSyndicate = await client.get(url=EntratiSyndicate_url)
        return EntratiSyndicate.text
#裂缝
async def get_fissures_api():
    fissures_url = 'http://nymph.rbq.life:3000/wf/robot/fissures'
    async with httpx.AsyncClient() as client:
        fissures = await client.get(url=fissures_url)
        return fissures.text
#打折
async def get_flashSales_api():
    flashSales_url = 'http://nymph.rbq.life:3000/wf/robot/flashSales'
    async with httpx.AsyncClient() as client:
        flashSales = await client.get(url=flashSales_url)
        return flashSales.text
#入侵
async def get_invasions_api():
    invasions_url = 'http://nymph.rbq.life:3000/wf/robot/invasions'
    async with httpx.AsyncClient() as client:
        invasions = await client.get(url=invasions_url)
        return invasions.text
#奸商
async def get_voidTrader_api():
    voidTrader_url = 'http://nymph.rbq.life:3000/wf/robot/voidTrader'
    async with httpx.AsyncClient() as client:
        voidTrader = await client.get(url=voidTrader_url)
        return voidTrader.text
#小小黑
async def get_persistentEnemies_api():
    persistentEnemies_url = 'http://nymph.rbq.life:3000/wf/robot/persistentEnemies'
    async with httpx.AsyncClient() as client:
        persistentEnemies = await client.get(url=persistentEnemies_url)
        return persistentEnemies.text
#地球
async def get_earthCycle_api():
    earthCycle_url = 'http://nymph.rbq.life:3000/wf/robot/earthCycle'
    async with httpx.AsyncClient() as client:
        earthCycle = await client.get(url=earthCycle_url)
        return earthCycle.text
#地球平原
async def get_cetusCycle_api():
    cetusCycle_url = 'http://nymph.rbq.life:3000/wf/robot/cetusCycle'
    async with httpx.AsyncClient() as client:
        cetusCycle = await client.get(url=cetusCycle_url)
        return cetusCycle.text
#舰队
async def get_constructionProgress_api():
    constructionProgress_url = 'http://nymph.rbq.life:3000/wf/robot/constructionProgress'
    async with httpx.AsyncClient() as client:
        constructionProgress = await client.get(url=constructionProgress_url)
        return constructionProgress.text
#金星平原
async def get_vallisCycle_api():
    vallisCycle_url = 'http://nymph.rbq.life:3000/wf/robot/vallisCycle'
    async with httpx.AsyncClient() as client:
        vallisCycle = await client.get(url=vallisCycle_url)
        return vallisCycle.text
#电波
async def get_nightwave_api():
    nightwave_url = 'http://nymph.rbq.life:3000/wf/robot/nightwave'
    async with httpx.AsyncClient() as  client:
        nightwave = await client.get(url=nightwave_url)
        return nightwave.text
#仲裁
async def get_arbitration_api():
    arbitration_url = 'http://nymph.rbq.life:3000/wf/robot/arbitration'
    async with httpx.AsyncClient() as client:
        arbitration = await client.get(url=arbitration_url)
        return arbitration.text
#火二平原
async def get_cambionCycle_api():
    cambionCycle_url = 'http://nymph.rbq.life:3000/wf/robot/cambionCycle'
    async with httpx.AsyncClient() as client:
        cambionCycle = await client.get(url=cambionCycle_url)
        return cambionCycle.text
#扎里曼
async def get_zarimanCycle_api():
    zarimanCycle_url = 'http://nymph.rbq.life:3000/wf/robot/zarimanCycle'
    async with httpx.AsyncClient() as client:
        zarimanCycle = await client.get(url=zarimanCycle_url)
        return zarimanCycle.text
#特价
async def get_dailyDeals_api():
    dailyDeals_url = 'http://nymph.rbq.life:3000/wf/robot/dailyDeals'
    async with httpx.AsyncClient() as client:
        dailyDeals = await client.get(url=dailyDeals_url)
        return dailyDeals.text



async def classify(msg: str):
    match msg:
        case '救命' | '菜单':
            return await directives()
        case '新闻':
            return await get_news_api()
        case '活动':
            return await get_events_api()
        case '警报':
            return await get_alerts_api()
        case '突击':
            return await get_sortie_api()
        case '地球赏金':
            return await get_Ostrons_api()
        case '金星赏金':
            return await get_Solaris_api()
        case '火卫二赏金':
            return await get_EntratiSyndicate_api()
        case '裂缝':
            return await get_fissures_api()
        case '打折':
            return await get_flashSales_api()
        case '入侵':
            return await get_invasions_api()
        case '奸商':
            return await get_voidTrader_api()
        case '小小黑':
            return await get_persistentEnemies_api()
        case '地球':
            return await get_earthCycle_api()
        case '地球平原':
            return await get_cetusCycle_api()
        case '舰队':
            return await get_constructionProgress_api()
        case '金星平原':
            return await get_vallisCycle_api()
        case '电波':
            return await get_nightwave_api()
        case '仲裁':
            return await get_arbitration_api()
        case '火卫二平原':
            return await get_cambionCycle_api()
        case '扎里曼':
            return await get_zarimanCycle_api()
        case '特价':
            return await get_dailyDeals_api()
