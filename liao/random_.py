# --coding: utf-8--
# 2017/8/9

'利用PIL模块生成随机验证码'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndchar():
	return chr(random.randint(65, 90))

# 随机颜色1
def rndcolor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndcolor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndcolor())
# 输出文字
list_text = []
for t in range(4):
	x = rndchar()
	draw.text((60 * t + 10, 10), x, font=font, fill=rndcolor2())
	list_text.append(x)
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
print list_text