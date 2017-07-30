# -- coding: utf-8 --

'generate a  simple image'

from PIL import Image
im = Image.open('github.jpg')
print im.format, im.size, im.mode
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')