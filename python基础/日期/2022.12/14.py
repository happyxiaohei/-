"""
14 - 字符串的内建函数

Date: 2022/12/16

"""

# 第一部分  关于大小写相关的

# capitalize
# title
# istitle
# upper
# lower
# islower




message = "zhaorui is a beautiful girl"


msg = message.capitalize()   # 将字符串的第一个字符串转成大写的标识形式
print(msg)


msg = message.title()    # 每个单词的首字母大写
print(msg)

msg = msg.istitle()
print(msg)

result = message.istitle() #返回的结果是布尔类型的,True,False
print(result)

msg = message.upper()   #将字符串全部转成大写的表示形式
print(msg)

result = msg.lower()  # 将大写全部转小写
print(result)

# 案例: 验证码案例

s = 'QWERTYUIOPASDFGHJKLZXCVBNMMqwertyuifdghxcvbmlsd098531323132'

print(len(s))    #求字符串的长度 len(str) ,返回值是一个整型的数值
# 四个随机数

code = ''

import random

# print(ran)
#
# print(s [ran])


for i in range(4):
    ran = random.randint(0, len(s) - 1)
    code += s[ran]  # code = code + V   ---->code = 'V'

print('验证码:' + code)

# 提示用户输入验证码

user_input = input('请输入验证码:')

if user_input.lower() == code .lower() :
    print('验证码输入正确')
else:
    print('验证码错误!')
















