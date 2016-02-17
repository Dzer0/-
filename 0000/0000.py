# coding:utf-8
from PIL import Image, ImageDraw, ImageFont

print '请输入你想输入的数字:'
num = raw_input()  # 读去用户输入的数字
im = Image.open('icon.jpg')
xsize, ysize = im.size  # 取图片长宽
ztfont = ImageFont.truetype('tianrandaimengziti.ttf', xsize // 5)  # 载入字体
tu = ImageDraw.Draw§(im)  # 载入图片
tu.text((xsize // 5 * 4, 0), num, fill='#ff0000', font=ztfont) #将文件写到图片上
im.save('new.jpg') #保存新图片
q = Image.open('new.jpg')
q.show()
