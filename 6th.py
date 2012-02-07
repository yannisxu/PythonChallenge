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

#第一部分为46145是最有一个文件，得到提示：Collect the comments.
#第二部分出现的图形为 HOCKEY 得到链接的下一句话是 it's in the air look at the letters，所以最终结果就是 拼出这些图形的字母：oxygen

import os,sys
import re 
import zipfile


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


zf = zipfile.ZipFile("sources/channel.zip")

id = "90052"
out = ""
while 1:
    text = zf.read("%s.txt" % id)
    match = re.compile("Next nothing is (\d*)").search(text)
    if match:
        out += zf.getinfo("%s.txt" % id).comment 
        id = match.group(1)
    else:
        break

print out 
