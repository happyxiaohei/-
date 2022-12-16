"""

10 -

Date: 2022/12/15

"""
'''
掷骰子
1.欢迎进入xxxx游戏
2.输入用户名,默认用户是没有币
3.提示用户充值买币(100块钱30币,充值必须是100的倍数,充值不成功可以再次充值)
4.玩一局游戏扣除2个币,猜大小(系统用随机数模拟骰子产生值)
5.只要猜对了奖励1个币,可以继续玩(想不想继续玩,也可以没有金币自动退出)
6.剩余10个币提醒.



'''


import random
print('*' * 30)
print('欢迎进入澳门赌场')
print('*' * 30)

username = input('请输入你的用户名:')
money = 0

# 判断 用户是否进入游戏   修改方案

# # answer = input('确定进入游戏吗? (y/n)')
# if answer == 'y':
# 在判断用户是否进入游戏时，应该使用一个while循环，直到用户输入'y'或'n'为止。


#  这种写法呢,用户输入其他数的直接就退出循环了

# while True:
#     answer = input('确定进入游戏吗? (y/n)')
#     if answer == 'y':
#         break
#     else:
#         print('退出游戏!!!!!')
#         exit()
#


# 而这种写法呢,用户输入错误后会继续循环

while True:
    answer = input('确定进入游戏吗? (y/n)')
    if answer == 'y':
        break
    elif answer == 'n':
        print('退出游戏!!!!!')
        exit()


# 判断游戏币是否充足   修改方案
     # 判断游戏币是否充足
#     while money <2 :
#
#         n = int(input('金币不足,请充值(100块钱等于30个游戏币,充值必须是100的倍数)'))
#         #充值金额判断
#         if n%100 == 0 and n>0 :
#             money= (n//100)*30
#
# 在判断金币数量是否足够时，应该使用一个while循环，直到用户充值后金币数量大于等于2为止。
while money < 2:
    n = int(input('金币不足,请充值(100块钱等于30个游戏币,充值必须是100的倍数)'))
    # 充值金额判断
    if n % 100 == 0 and n > 0:
        money = (n // 100) * 30

# print('当前游戏币是:{},玩一局游戏扣除游戏币2个'.format(money))
# 打印当前的金币数量
print('当前游戏币是:{},玩一局游戏扣除游戏币2个'.format(money))


# print('进入游戏.......')
# 进入游戏
print('进入游戏.......')


while True:

    # 模拟骰子 产生骰子的值
    t1 = random.randint(1, 6)
    t2 = random.randint(1, 6)

    # 设定两个骰子的值,大于6 等于大,否则就是小

    money -= 2  # 扣除金币
    print('您的金币余额为{}'.format(money))
    print('系统洗牌完毕,请猜大小:')

    # 读取用户输入
    guess = input('请输入大或者小(大,输入1,小,输入0):')

    # 判断

    print(money)
    if ((t1 + t2) > 6 and guess == "1") or ((t1 + t2) < 6 and guess == "0"):
        # print(t1,t2 )
        print('您猜对了，两个骰子的值分别是{}和{}'.format(t1, t2))

        print('恭喜{}!本局游戏获得奖励1个游戏币.!!!'.format(username))

        # 在奖励金币时，应该将金币数量加1，而不是赋值为1。
        # 奖励金币
        money += 1
    else:
        # print('很遗憾!本局游戏输了.....')
        print('您猜错了，两个骰子的值分别是{}和{}'.format(t1, t2))
        # 在打印猜大小的结果时，应该打印出两个骰子的值。
        print('很遗憾!本局游戏输了.....')
    # 在打印结果时，应该区分胜利和失败的情况，并打印相应的信息。

    # 在判断用户是否继续游戏时，应该使用一个while循环，直到用户输入'y'或者金币数量不足为止。

    # answer = input('是否继续再来一局游戏,要扣除2枚游戏币?(y/n)')
    # while answer !='y'or money >2 :
    #
    #     print('退出游戏!!!!!')
    #
    #     break

    # 判断用户是否继续游戏
    while True:
        answer = input('是否继续再来一局游戏,要扣除2枚游戏币?(y/n)')
        if answer == 'y' and money >= 2:
            break
        elif answer != 'y' or money < 2:
            print('退出游戏!!!!!')
            exit()
