######################################################################
## Filename:      6th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Feb 03 23:59:42 2012
##                
## Description:   
##                
######################################################################

#46145是最有一个文件，得到提示：Collect the comments.

import os,sys
import re 


list = os.walk("sources/channel/")

filenum = 0
for root,dirs,file in list:
    for f in file:
        filenum+=1
        print filenum


startnum="90052"

for i in range(filenum):
    f = open("sources/channel/"+startnum+".txt","r")
    content = f.read()
    p = re.compile(r'(\d+)')
    start = p.findall(content)
    for i in start:
        startnum = i
        print startnum
