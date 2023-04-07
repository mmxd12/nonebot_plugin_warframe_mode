#看着可能有点乱

import nonebot
import urllib.parse
from httpx import AsyncClient
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent


from .data_source import wfapi

#指令
warframe = nonebot.on_command("wf", aliases={"救命","菜单"}, priority=5)
news = nonebot.on_command("新闻")
events = nonebot.on_command("活动")
alerts = nonebot.on_command("警报")
sortie = nonebot.on_command("突击")
Ostrons = nonebot.on_command("地球赏金")
Solaris = nonebot.on_command("金星赏金")
EntratiSyndicate = nonebot.on_command("火二赏金")
fissures = nonebot.on_command("裂缝")
flashSales = nonebot.on_command("打折")
invasions = nonebot.on_command("入侵")
voidTrader = nonebot.on_command("奸商")
persistentEnemies = nonebot.on_command("小小黑")
earthCycle = nonebot.on_command("地球")
cetusCycle = nonebot.on_command("地球平原")
constructionProgress = nonebot.on_command("舰队")
vallisCycle = nonebot.on_command("金星平原")
nightwave = nonebot.on_command("电波")
arbitration = nonebot.on_command("仲裁")
cambionCycle = nonebot.on_command("火二平原")
zarimanCycle = nonebot.on_command("扎里曼")
dailyDeals = nonebot.on_command("特价")

@warframe.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    wf_msg = await wfapi.directives()

    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": wf_msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@news.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    news_msg = await wfapi.news()

    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": news_msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@events.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    events_msg = await wfapi.events()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": events_msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@alerts.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    alerts_msg = await wfapi.alerts()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": alerts_msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@sortie.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.sortie()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@Ostrons.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.Ostrons()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@Solaris.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.Solaris()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@EntratiSyndicate.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.EntratiSyndicate()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@fissures.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.fissures()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@flashSales.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.flashSales()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@invasions.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.invasions()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@voidTrader.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.voidTrader()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@persistentEnemies.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.persistentEnemies()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@earthCycle.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.earthCycle()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@cetusCycle.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.cetusCycle()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@constructionProgress.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.constructionProgress()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@vallisCycle.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.vallisCycle()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@nightwave.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.nightwave()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@arbitration.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.arbitration()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@cambionCycle.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.cambionCycle()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@zarimanCycle.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.zarimanCycle()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

@dailyDeals.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.dailyDeals()
    msg_list = []
    msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": msg
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=msg_list)

###以下为需要搜索词指令

#wm市场
wm = nonebot.on_command('wm', aliases={'查询'}, block=True)
@wm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    txt = msg.extract_plain_text().strip()
    url = f'http://nymph.rbq.life:3000/wm/robot/{txt}'
    message = await wm_api(url)
    wm_msg_list = []
    wm_msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": f"本次查询：{txt}\n"+message
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=wm_msg_list)
    #await wm.finish(message)

async def wm_api(url):
    async with AsyncClient() as client:
        res = (await client.get(url))
        return res.text


#rm紫卡
rm = nonebot.on_command('rm', aliases={'紫卡'}, block=True)
@rm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    rm_txt = msg.extract_plain_text().strip()
    rm_url = f'http://nymph.rbq.life:3000/rm/robot/{rm_txt}'
    message_rm = await rm_api(rm_url)
    rm_msg_list = []
    rm_msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": f"本次查询：{rm_txt}\n"+message_rm
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=rm_msg_list)
    #await rm.finish(message_rm)

async def rm_api(rm_url):
    async with AsyncClient() as client:
        res_rm = (await client.get(rm_url))
        return res_rm.text


#中英翻译
tran = nonebot.on_command('tran', aliases={'翻译'}, block=True)
@tran.handle()
async def _(bot:Bot, event: GroupMessageEvent,msg: Message = CommandArg()):
    tran_txt = msg.extract_plain_text().strip()
    tran_url = f'http://nymph.rbq.life:3000/dict/tran/robot/{tran_txt}'
    message_tran = await tran_api(tran_url)
    tran_msg_list = []
    tran_msg_list.append(
        {
            "type": "node",
            "data": {
                "name": "这里是WFBOT",
                "uin": event.self_id,
                "content": f"本次翻译：{tran_txt}\n"+message_tran
            }
        }
    )
    await bot.call_api('send_group_forward_msg', group_id=event.group_id, messages=tran_msg_list)
    #await tran.finish(message_tran)

async def tran_api(tran_url):
    async with AsyncClient() as client:
        res_tran = (await client.get(tran_url))
        return res_tran.text


#wiki
wiki = nonebot.on_command('wiki', aliases={'维基'}, block=True)
@wiki.handle()
async def _(msg: Message = CommandArg()):
    txt = msg.extract_plain_text().strip()
    new_txt = urllib.parse.quote(txt)
    url = f'这是您找的{txt}\n请复制到浏览器打开!\n\nhttps://warframe.huijiwiki.com/wiki/{new_txt}'
    await wiki.finish(message=url)
