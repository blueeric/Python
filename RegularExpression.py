#-*-coding:utf8-*-
import re
#from re import findall,search,S

secret_code ="hadkfalifexxIxxfasdjdksdfjsd123xxlovexxswdfjhsifixxyouxxsdfsf"

secret_code2 ='''djdksdfjsd123xx
lovexxswdfjhsifixxyouxxsdfsf'''

#.的使用
a ='xz1234'
b = re.findall('x.',a)
print b


#*的用法
a1 = 'xz123'
b1 = re.findall('x*',a1)
print b1

#?的使用
a2 = 'xz123'
b2 = re.findall('x??',a2)
print b2

#.*
b3= re.findall('xx(.*)xx',secret_code)
print b3

#.*?
b3= re.findall('xx(.*?)xx',secret_code)
print b3

#S
b4 = re.findall('xx(.*?)xx',secret_code2,re.S)
print str(b4)+str("=")


#对比findall与search区别
s2= 'asdfxxIxx123xxlovexxdfd'
f = re.search('xx(.*?)xx123xx(.*?)xx',s2).group(2)
print f

#findall
s2 = "asdfxxIxx123xxlovexxdfd"
f2 = re.findall('xx(.*?)xx123xx(.*?)xx',s2)
print f2[0][1]


#sub 的使用
s3= '123sdfasdfasdfasdfasfd123'
f3 = re.sub('123(.*?)123','123dddddddd123',s3)
print f3

#匹配数字
a4= 'asd123sdf123adf3456'
f4 = re.findall('(\d+)',a4)
print f4