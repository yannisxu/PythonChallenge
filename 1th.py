######################################################################
## Filename:      0th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Fri Jan 13 01:18:21 2012
##                
## Description:   
##                
######################################################################
#题目说明，根据题目的提示，将每个字符向后移动两位，得到信息：
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url
#应用于 map -> ocr    最后答案为ocr.html
def convert(str):
    newstr="";
    for char in str:
        if(char>='a'and char<='x'):             #当字符是在a,x中间的一个，则向后移动两位
            newstr+=chr(ord(char)+2);
        else:
            if(char>='y' and char<='z'):        #当字符是y,z中的一个，则字符转化为a,b
                newstr+=chr(ord(char)-24);
            else:                               #如果是其他字符则不变
                newstr+=char;
    return newstr;

if __name__ == "__main__":
    #print "main function";
    str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj";
    newstr=convert(str);
    print newstr;
        
    
    
