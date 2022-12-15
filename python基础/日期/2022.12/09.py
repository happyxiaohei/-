"""
09 -

Date: 2022/12/14

"""
'''

while:  关键字   完成循环

while  条件:
    语句体(块)
else :
    语句体(块)

    '''
# i = 1
# while i <= 10:
#     print(i)
#     i+=2
#
#

#  打印1-30之间的所有3的倍数
#
# n = 1
# while n <= 30:
#     #进入循环体
#     if n%3 ==0:
#         print('-----',n)
#         # 改变n
#     n+=1


#  打印1-30之间的所有3的倍数

# n = 1
# while n <= 30:
#     #进入循环体
#     if n%3 ==0 and n %5 == 0 :
#         print('-----',n)
#         # 改变n的值
#     n+=1
#

'''


使用while循环计算1-20的累加和

1+2+3+4.....20

'''
# sum_1 = 0
# i = 1
# while i <= 20:
#     sum_1 += i
#     i += 1
#
# print('-------累加和是:',sum_1)
#

'''

打印三角形
'''

'''
1.分析:
1.层数明确
2.发现规律  层数与个数
3,用什么表示层,用什么表示*的个数

'''

# ceng = 1
#
# while ceng <=5 :
#     #   打印*号
#     # print('*' * ceng)
#     #嵌套while循环
#
#     count = 1
#     while count<=ceng:
#         print("*",end = '')
#         count +=1
#
#
#     ceng += 1
#     print()   #换行

# 九九乘法表
import random
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, '*', i, '=', j * i, '', end='')
        j += 1
    print()
    i += 1


ceng = 1
while ceng <= 9:
    count = 1
    while count <= ceng:
        print('{}*{}={}'.format(count, ceng, count * ceng), ' ', end='')
        count += 1
    print()
    ceng += 1


#
# print('--------------')
# ceng = 5
# while ceng >= 0 :
#
#
#     ceng -= 1
#
#


'''
掷骰子
1.欢迎进入xxxx游戏
2.输入用户名,默认用户是没有币
3.提示用户充值买币(100块钱30币,充值必须是100的倍数,充值不成功可以再次充值)
4.玩一局游戏扣除2个币,猜大小(系统用随机数模拟骰子产生值)
5.只要猜对了奖励1个币,可以继续玩(想不想继续玩,也可以没有金币自动退出)
6.剩余10个币提醒.



'''

#


