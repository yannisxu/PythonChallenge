######################################################################
## Filename:      3th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Jan 27 15:28:23 2012
##                
## Description:   
##                
######################################################################

#答案linkedlist

import re 

f=open("sources/3.txt","r")
text=f.read()
text.strip()

p=re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
print p.findall(text)
