#本指令api均来自：https://github.com/WsureWarframe/warframe-info-api
#群号435021808
#这边为消息发送除了wm/rm/tran(翻译）这三个因为要获取信息所以在这边写

import urllib.parse   #url编码
from nonebot import on_command
from nonebot.internal.adapter import Message
from nonebot.adapters.onebot.v11 import Bot,GroupMessageEvent
from nonebot.params import CommandArg
from httpx import AsyncClient

from .data_source import classify,directives

warframe = on_command("warframe", aliases={"", "/"},priority=5)

@warframe.handle()
async def receive(bot:Bot, event: GroupMessageEvent,args: Message = CommandArg()):
    msg = await classify(args.extract_plain_text())

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
    #await warframe.finish(message=msg)


#wm市场
wm = on_command('wm',aliases={'wm','/wm'},priority=5,block=True)
@wm.handle()
async def _(bot:Bot, event: GroupMessageEvent,msg: Message = CommandArg()):
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
rm = on_command('rm',aliases={'rm','/rm'},priority=5,block=True)
@rm.handle()
async def _(bot:Bot, event: GroupMessageEvent,msg: Message = CommandArg()):
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
tran = on_command('tran',aliases={'tran','翻译'},priority=5,block=True)
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
wiki = on_command('wiki', aliases={'wiki','维基'}, block=True)
@wiki.handle()
async def _(msg: Message = CommandArg()):
    txt = msg.extract_plain_text().strip()
    new_txt = urllib.parse.quote(txt)
    url = f'这是您找的{txt}\n请复制到浏览器打开!\n\nhttps://warframe.huijiwiki.com/wiki/{new_txt}'
    await wiki.finish(message=url)


