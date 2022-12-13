"""
07 - 

Date: 2022/12/13

"""

# 随机数 :

import  random
ran = (random.randint(1, 10))

'''
猜大小
步骤:
1.系统产生一个随机数
2.键盘输入一个数
3.将系统产生的与你键盘输入的进行比较
4.猜对了,中大奖   猜错了  拜拜  下次再来

'''
# print(('*' * 10, '猜数字', '*' * 10))
# figure = int(input('请输入(1-10)你要猜的数字('))
# if figure == ran:
#     print('恭喜你猜对了,中大奖')
# else:
#     print('猜错了.拜拜')
# print('数字是{}'.format(ran))
# print('游戏结束')
#

'''

多层条件判断:
if 100-90:
    优+
elif 90-80
    优-
elif 80-70
    良
elif 70-60
    及格
else 
    不及格
'''

age = int(input('请猜猜年龄'))
if age <=18 and age > 0 :
    print('太有眼光了')
elif age >18 and age <=30:
    print('人家还是宝宝呢')
elif age >30 and age <=40 :
    print('长得泰年轻了吧')
else:
    print('输入错误!')



'''
4中结构
if 条件:
    语句
    
    
--------------

if 条件 :
    语句
else:
    语句
    
-----------------

if 条件1:
    ....
    if 条件2 
        语句
    else :
        ......
        
        
        
--------------------


if 条件 1 :
    语句
elif 条件2:
    语句
leif 条件3
    语句
    ..........
else:
    语句
    
    
    '''