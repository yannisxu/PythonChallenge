######################################################################
## Filename:      11th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Mar 02 20:06:08 2012
##                
## Description:   
##                
######################################################################

import Image

img = Image.open("sources/cave.jpg")
weight, height = img.size

odd = even = Image.new(img.mode, (weight/2, height/2)) 
for x in range(weight):
    for y in range(height):
        if(x + y*weight)%2:              #判断像素坐标的奇偶
            odd.putpixel((x/2,y/2), img.getpixel((x,y)))
        else:
            even.putpixel((x/2,y/2), img.getpixel((x,y)))

odd.save("sources/odd.jpg")
even.save("sources/even.jpg")
