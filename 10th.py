######################################################################
## Filename:      10th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Wed Feb 29 06:51:40 2012
##                
## Description:   
##                
######################################################################

#查看源代码，根据提示 打开sequence.txt, 看到的结果是 a=[1, 11, 21, 1211, 111221 , 根据bull.html页面的提示 len(a[30]) 求解
#数字的规律是后一个描述前一个，比如 11指前面1个1，21是指前面2个1，1211是指前面1个2，1个1，111221指前面1个1，1个2，2个1，根据提示得出312211

import string

startstr = "1"
count = 0
newstr = ""

for i in range(30):
    temp = startstr[0]
    for j in startstr:
        if temp == j:
            count += 1
        else:
            if count == 0:
                count += 1
            newstr += str(count)
            newstr += temp
            count = 1
            temp = j
            
    newstr += str(count)
    newstr += temp
    count = 0
        
    print "第 %d 次循环" %(i)
    print newstr
    startstr = newstr
    newstr = ""

print "结果为"
print len(startstr)
