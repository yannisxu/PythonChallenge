######################################################################
## Filename:      8th.py
##                
## Copyright (c) 2012,Yannis
## Version:       
## Author:        Yannis.Xu <excellentbright@gmail.com>
## Created at:    Sat Feb 11 17:13:49 2012
##                
## Description:   
##                
######################################################################

#本题当中查看源代码得到一串加密字符，根据提示用bz2进行解码
#点击图片中的蜜蜂，就会要求输入用户名和密码，将解密的用户名和密码输入即可

import bz2

user = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"

password = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

deuser = bz2.decompress(user)
depassword = bz2.decompress(password)

print repr(deuser)
print repr(depassword)
