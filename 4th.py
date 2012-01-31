######################################################################
## Filename:      4th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Tue Jan 31 21:04:39 2012
##                
## Description:   
##                
######################################################################

#获取到16044之后，出现divide by two 中断
#答案是peak.html

import urllib
import re 

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
#num='12345'
#num='8022'
num='87890'

for i in range(100):
    page=urllib.urlopen(url+num)
    file=page.read()
    p=re.compile(r'(\d+)')
    numlist=p.findall(file)
    for i in numlist:
        num=i
    print num 
