#本指令api均来自：https://github.com/WsureWarframe/warframe-info-api
#群号435021808
#这边为消息发送除了wm/rm/tran(翻译）这三个因为要获取信息所以在这边写
from nonebot import on_command
from nonebot.internal.adapter import Message
from nonebot.params import CommandArg
from httpx import AsyncClient
from .data_source import classify,directives

WF = on_command("WF", aliases={"#", "/"},priority=5)

@WF.handle()
async def receive(args: Message = CommandArg()):
    msg = await classify(args.extract_plain_text())
    await WF.finish(message=msg)


#wm市场
wm = on_command('wm',aliases={'wm','/wm'},priority=5,block=True)
@wm.handle()
async def _(msg: Message = CommandArg()):
    txt = msg.extract_plain_text().strip()
    url = f'http://nymph.rbq.life:3000/wm/robot/{txt}'
    message = await wm_api(url)
    await wm.finish(message)

async def wm_api(url):
    async with AsyncClient() as client:
        res = (await client.get(url))
        return res.text


#rm紫卡
rm = on_command('rm',aliases={'rm','/rm'},priority=5,block=True)
@rm.handle()
async def _(msg: Message = CommandArg()):
    rm_txt = msg.extract_plain_text().strip()
    rm_url = f'http://nymph.rbq.life:3000/rm/robot/{rm_txt}'
    message_rm = await rm_api(rm_url)
    await rm.finish(message_rm)

async def rm_api(rm_url):
    async with AsyncClient() as client:
        res_rm = (await client.get(rm_url))
        return res_rm.text


#中英翻译
tran = on_command('tran',aliases={'tran','翻译'},priority=5,block=True)
@tran.handle()
async def _(msg: Message = CommandArg()):
    tran_txt = msg.extract_plain_text().strip()
    tran_url = f'http://nymph.rbq.life:3000/dict/tran/robot/{tran_txt}'
    message_tran = await tran_api(tran_url)
    await tran.finish(message_tran)

async def tran_api(tran_url):
    async with AsyncClient() as client:
        res_tran = (await client.get(tran_url))
        return res_tran.text