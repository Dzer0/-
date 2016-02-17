# coding:utf-8
from PIL import Image, ImageDraw, ImageFont

print '请输入你想输入的数字:'
num = raw_input()   #读去用户输入的数字


im = Image.open('icon.jpg')
xsize, ysize = im.size
ztfont = ImageFont.truetype('tianrandaimengziti.ttf', xsize // 5)
tu = ImageDraw.Draw§(im)
tu.text((xsize // 5 * 4, 0), num, fill='#ff0000', font=ztfont)
im.save('new.jpg')
q = Image.open('new.jpg')
q.show()