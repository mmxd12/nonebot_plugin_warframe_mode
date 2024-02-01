# 看着更简单
from httpx import AsyncClient
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
import os
from io import BytesIO


async def get_data_api(url_arg):
    api_url = f'http://nymph.rbq.life:3000/wf/robot/{url_arg}'
    async with AsyncClient() as client:
        r = (await client.get(api_url))
        return r.text
    

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

def draw_text_on_image(text, font_path, font_size, bg_color, border_color, border_width, image_path):
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

#长图
def text_on_image(data):
    font_size = 20
    # 创建绘制对象

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)

    # 创建一个透明的图像
    image = Image.new('RGB', (1, 1), color=(0,0,0)) # type: ignore
    draw = ImageDraw.Draw(image)

    # 计算文本的宽度和高度
    text_width, text_height = draw.textsize(data, font) # type: ignore

    # 创建一个与文本大小匹配的图像
    image = Image.new('RGB', (text_width, text_height), color=(255,255,255)) # type: ignore
    draw = ImageDraw.Draw(image)

    # 在图像上绘制文本
    draw.text((0, 0), data, font=font, fill=(0, 0, 0))
    image = image.filter(ImageFilter.SHARPEN)

    # 将图片保存为字节流
    bytes_io = BytesIO()
    image.save(bytes_io, format='JPEG')

    return bytes_io



dic = [(
        "所有指令请艾特机器人可加前缀</>也可不加"
        '\n一下为warframe指令：'
        '\nwm <搜索词>'
        '\nrm <搜索词>'
        '\nwr/zk <搜索词>'
        '\nxh/玄骸 <搜索词>'
        "\nwiki <搜索词>"
        '\n翻译 <搜索词>'
        '\n打折|小小黑|特价'
        '\n新闻| 事件 |警报'
        '\n突击| 裂缝 |入侵'
        '\n奸商| 特价 |地球'
        '\n电波| 仲裁 |扎里曼'
        '\n地球赏金|金星赏金|火卫二赏金'
        '\n火卫二平原|金星平原|地球平原'
        '\n泡茶|泡茶表/泡茶查询|等级/等级表'
        '\n小浅<要提问的问题>/问<要问的问题>'
    )]

class wfapi:

    # 菜单指令
    @classmethod
    async def directives(cls):
        return dic[0]
    
    # 新闻
    @classmethod
    async def news(cls):
        text = await get_data_api("news")
        iamge = text_on_image(text)
        return iamge

    # 活动
    @classmethod
    async def events(cls):
        data = await get_data_api("events")
        imgae = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return imgae

    # 警报
    @classmethod
    async def alerts(cls):
        data = await get_data_api("alerts")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 突击
    @classmethod
    async def sortie(cls):
        data = await get_data_api("sortie")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 地球赏金
    @classmethod
    async def Ostrons(cls):
        data = await get_data_api("Ostrons")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 金星赏金
    @classmethod
    async def Solaris(cls):
        data = await get_data_api("Solaris")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 火二赏金
    @classmethod
    async def EntratiSyndicate(cls):
        data = await get_data_api("EntratiSyndicate")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 裂缝
    @classmethod
    async def fissures(cls):
        data = await get_data_api("fissures")
        image = text_on_image(data)
        return image

    # 打折
    @classmethod
    async def flashSales(cls):
        data = await get_data_api("flashSales")
        image = text_on_image(data)
        return image

    # 入侵
    @classmethod
    async def invasions(cls):
        data = await get_data_api("invasions")
        image = text_on_image(data)
        return image

    # 奸商
    @classmethod
    async def voidTrader(cls):
        data = await get_data_api("voidTrader")
        image = text_on_image(data)
        return image

    # 小小黑
    @classmethod
    async def persistentEnemies(cls):
        data = await get_data_api("persistentEnemies")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 地球
    @classmethod
    async def earthCycle(cls):
        data = await get_data_api("earthCycle")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 地球平原
    @classmethod
    async def cetusCycle(cls):
        data = await get_data_api("cetusCycle")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 舰队
    @classmethod
    async def constructionProgress(cls):
        data = await get_data_api("constructionProgress")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 金星平原
    @classmethod
    async def vallisCycle(cls):
        data = await get_data_api("vallisCycle")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 电波
    @classmethod
    async def nightwave(cls):
        data = await get_data_api("nightwave")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 仲裁
    @classmethod
    async def arbitration(cls):
        data = await get_data_api("arbitration")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 火二平原
    @classmethod
    async def cambionCycle(cls):
        data = await get_data_api("cambionCycle")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 扎里曼
    @classmethod
    async def zarimanCycle(cls):
        data = await get_data_api("zarimanCycle")
        image = draw_text_on_image(data, font_path, 25, (220, 220, 220, 220), (255, 0, 0), 2, image_path)
        return image

    # 特价
    @classmethod
    async def dailyDeals(cls):
        data = await get_data_api("dailyDeals")
        image = text_on_image(data)
        return image