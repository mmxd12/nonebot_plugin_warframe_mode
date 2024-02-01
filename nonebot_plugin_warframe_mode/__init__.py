# 看着可能有点乱
import os
import nonebot
import urllib.parse
from httpx import AsyncClient
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, GroupMessageEvent
from .data_source import wfapi
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random



# 指令
warframe = nonebot.on_command("wf", aliases={"救命", "菜单"}, priority=5)
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
async def receive_warframe(bot:Bot,event:GroupMessageEvent):
    wf_msg = await wfapi.directives()
    await warframe.finish(message=wf_msg)


@news.handle()
async def receive_news(bot:Bot,event:GroupMessageEvent):
    news_msg = await wfapi.news()
    await news.send(message=MessageSegment.image(news_msg))


@events.handle()
async def receive_events():
    events_msg = await wfapi.events()
    await events.send(message=MessageSegment.image(events_msg))


@alerts.handle()
async def receive_alerts(bot: Bot, event: GroupMessageEvent):
    alerts_msg = await wfapi.alerts()
    await alerts.finish(message=MessageSegment.image(alerts_msg))


@sortie.handle()
async def receive_sortie(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.sortie()
    await sortie.finish(message=MessageSegment.image(msg))


@Ostrons.handle()
async def receive_Ostrons(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.Ostrons()
    await Ostrons.finish(message=MessageSegment.image(msg))


@Solaris.handle()
async def receive_Solaris(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.Solaris()
    await Solaris.finish(message=MessageSegment.image(msg))


@EntratiSyndicate.handle()
async def receive_EntratiSyndicate(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.EntratiSyndicate()
    await EntratiSyndicate.finish(message=MessageSegment.image(msg))


@fissures.handle()
async def receive_fissures(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.fissures()
    await fissures.finish(message=MessageSegment.image(msg))


@flashSales.handle()
async def receive_flashSales(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.flashSales()
    await flashSales.finish(message=MessageSegment.image(msg))


@invasions.handle()
async def receive_invasions(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.invasions()
    await invasions.finish(message=MessageSegment.image(msg))


@voidTrader.handle()
async def receive_voidTrader(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.voidTrader()
    await voidTrader.finish(message=MessageSegment.image(msg))


@persistentEnemies.handle()
async def receive_persistentEnemies(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.persistentEnemies()
    await persistentEnemies.finish(message=MessageSegment.image(msg))


@earthCycle.handle()
async def receive_earthCycle(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.earthCycle()
    await earthCycle.finish(message=MessageSegment.image(msg))


@cetusCycle.handle()
async def receive_cetusCycle(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.cetusCycle()
    await cetusCycle.finish(message=MessageSegment.image(msg))


@constructionProgress.handle()
async def receive_constructionProgress(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.constructionProgress()
    await constructionProgress.finish(message=MessageSegment.image(msg))


@vallisCycle.handle()
async def receive_vallisCycle(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.vallisCycle()
    await vallisCycle.finish(message=MessageSegment.image(msg))


@nightwave.handle()
async def receive_nightwave(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.nightwave()
    await nightwave.finish(message=MessageSegment.image(msg))


@arbitration.handle()
async def receive_arbitration(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.arbitration()
    await arbitration.finish(message=MessageSegment.image(msg))


@cambionCycle.handle()
async def receive_cambionCycle(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.cambionCycle()
    await cambionCycle.finish(message=MessageSegment.image(msg))


@zarimanCycle.handle()
async def receive_zarimanCycle(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.zarimanCycle()
    await zarimanCycle.finish(message=MessageSegment.image(msg))


@dailyDeals.handle()
async def receive(bot: Bot, event: GroupMessageEvent):
    msg = await wfapi.dailyDeals()
    await dailyDeals.finish(message=MessageSegment.image(msg))

# # # 以下为需要搜索词指令

#字体
font_file = 'zt.ttf'
current_dir = os.path.dirname(__file__)
font_path = os.path.join(current_dir, font_file)

# 图片路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "image/")
# 图片列表
image_files = os.listdir(IMAGE_PATH)
image_file = random.choice(image_files)
image_path = os.path.join(IMAGE_PATH,image_file)

def text_to_image(text, font_path, font_size, bg_color, border_color, border_width, image_path):
    # 创建一个透明的图片
    img = Image.new('RGBA', (1, 1), (0, 0, 0, 0)) # type: ignore
    draw = ImageDraw.Draw(img)

    # 设置字体
    font = ImageFont.truetype(font_path, font_size)

    # 计算文本宽度和高度
    text_width, text_height = draw.textsize(text, font)

    # 创建一个适配文本宽度和高度的灰色图片
    img = Image.new('RGBA', (text_width + 2 * border_width, text_height + 2 * border_width), bg_color)

    # 添加自定义底图
    if image_path:
        custom_image = Image.open(image_path).convert('RGBA')
        custom_image = custom_image.resize((text_width + 2 * border_width, text_height + 2 * border_width),
                                        Image.ANTIALIAS)
        img = Image.alpha_composite(img, custom_image)

    # 添加模糊效果
    img = img.filter(ImageFilter.GaussianBlur(radius=2))


    # 添加渐变色边框
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (img.width - 1, img.height - 1)], outline=border_color, width=border_width)

    # 在图片上写入文本
    draw.text((border_width, border_width), text, font=font, fill=(218, 112, 214))

    # 锐化图片
    img = img.filter(ImageFilter.SHARPEN)

    # 锐化文本
    text_img = img.crop((border_width, border_width, text_width + border_width, text_height + border_width))
    text_img = text_img.filter(ImageFilter.SHARPEN)
    img.paste(text_img, (border_width, border_width))

    #转为字节流方便发送
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    return img_bytes


# wm市场
wm = nonebot.on_command('wm', aliases={'查询'}, block=True)
@wm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    txt = msg.extract_plain_text()
    url = f'http://nymph.rbq.life:3000/wm/robot/{txt}'
    message = await wm_api(url)
    text = text_to_image(message, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
    await wm.finish(message=MessageSegment.image(text))


async def wm_api(url):
    async with AsyncClient() as client:
        res = (await client.get(url))
        return res.text


# rm紫卡
rm = nonebot.on_command('rm', aliases={'紫卡'}, block=True)
@rm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    rm_txt = msg.extract_plain_text()
    rm_url = f'http://nymph.rbq.life:3000/rm/robot/{rm_txt}'
    message_rm = await rm_api(rm_url)
    text = text_to_image(message_rm, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
    await rm.finish(message=MessageSegment.image(text))


async def rm_api(rm_url):
    async with AsyncClient() as client:
        res_rm = (await client.get(rm_url))
        return res_rm.text
    
#wmr紫卡
wmr = nonebot.on_command('wmr', aliases={'wr','zk'}, block=True)
@wmr.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    wmr_txt = msg.extract_plain_text()
    wmr_url = f'http://nymph.rbq.life:3000/wmr/robot/{wmr_txt}'
    message_wmr = await wmr_api(wmr_url)
    text = text_to_image(message_wmr, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
    await wmr.finish(message=MessageSegment.image(text))

async def wmr_api(wmr_url):
    async with AsyncClient() as client:
        res_wmr = (await client.get(wmr_url))
        return res_wmr.text
    
# wmw玄骸
wmw = nonebot.on_command('wmw', aliases={'xh','玄骸'}, block=True)
@wmw.handle()
async def _(bot:Bot, event: GroupMessageEvent,msg: Message = CommandArg()):
    wmw_txt = msg.extract_plain_text()
    wmw_url = f'http://nymph.rbq.life:3000/wmw/robot/{wmw_txt}'
    message_wmw = await wmw_api(wmw_url)
    text = text_to_image(message_wmw, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
    await wmw.finish(message=MessageSegment.image(text))

async def wmw_api(wmw_url):
    async with AsyncClient() as client:
        res_wmw = (await client.get(wmw_url))
        return res_wmw.text


# 中英翻译
tran = nonebot.on_command('tran', aliases={'翻译'}, block=True)


@tran.handle()
async def _(bot:Bot, event: GroupMessageEvent,msg: Message = CommandArg()):
    tran_txt = msg.extract_plain_text()
    tran_url = f'http://nymph.rbq.life:3000/dict/tran/robot/{tran_txt}'
    message_tran = await tran_api(tran_url)
    await tran.finish(message_tran)

async def tran_api(tran_url):
    async with AsyncClient() as client:
        res_tran = (await client.get(tran_url))
        return res_tran.text


# wiki
wiki = nonebot.on_command('wiki', aliases={'维基'}, block=True)

@wiki.handle()
async def _(msg: Message = CommandArg()):
    txt = msg.extract_plain_text()
    new_txt = urllib.parse.quote(txt)
    url = f'这是您找的{txt}\n请复制到浏览器即可打开!\n\nhttps删://删warframe.删huijiwiki.删com/删wiki/{new_txt}'
    await wiki.finish(message=url)
