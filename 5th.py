######################################################################
## Filename:      5th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Feb 03 14:49:07 2012
##                
## Description:   
##                
######################################################################

#本题需要使用pickle对文本进行序列化，然后作为图形输出
#输出答案为 channel  
import pickle

f = file("sources/banner.p","r")
data = open("sources/banner.p","r")    
datas = data.read()              #为序列化文本
newdata = pickle.load(f)         #序列化文本

string=""
for elt in newdata:
    for e in elt:
	string+=e[0]*e[1]
    string+="\n"
print string
