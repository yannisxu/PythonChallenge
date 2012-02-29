######################################################################
## Filename:      7th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Thu Feb 09 13:16:59 2012
##                
## Description:   
##                
######################################################################

#首先用GIMP将灰色部分抠出来，然后放大，可以观察到每个像素的灰度是7个像素，接下去读取灰度数值，转化为ascii码
#最后答案为integrity

import Image

img = Image.open('sources/oxygen.png')

#像素的参数: left,top,right,bottom
area = (0, 43, 608, 52)

#切割图片
cut = img.crop(area)

pixels = cut.getdata()

#输出图片模式和总的像素量以及第一个像素点的位置
print " mode: %s \n amount of pixel: %d" % (img.mode,len(pixels))
print pixels[0]

#转化为L模式
lcut = cut.convert('L')

lpixels = lcut.getdata()


str = []
#根据我们判断的7像素
for i in range(0, 608, 7):
    str.append(chr(lpixels[i]))         #转化为字符

#print str 通过join处理输出结果
print ''.join(str)

#输出结果为 smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(chr(x) for x in result)
