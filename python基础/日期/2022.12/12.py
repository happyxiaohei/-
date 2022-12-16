import random
"""
12 -

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

print('*' * 40)
print('欢迎进入猜大小游戏')
print('*' * 40)


username = input('请输入你的用户名:')
money = 0

# 判断用户是否需要进入游戏

while True:
    jinru = int(input('确定进入游戏吗? (0/1)'))
    if jinru == 1:
        break
    elif jinru == 0:
        print('游戏结束!')
        exit()


# 判断是否拥有游戏币
while money < 3:
    n = int(input('游戏币不足,请充值(100等于50个币,充值金额必须是100的倍数)'))

 # 判断充值金额是否正确
    if n % 100 == 0 and n > 0:
        money = (n / 100) * 50

# 打印当前游戏币数量
print('当前余额为{}个游戏币,每局游戏消耗两个游戏币.'.format(money))


# 进入游戏判断
print('进入游戏.......')
while True:
    money -= 2  # 进入游戏后扣除游戏币
    q1 = random.randint(1, 6)
    q2 = random.randint(1, 6)

    print('您当前金币余额为{}个游戏币.'.format(money))
    print('系统重置骰子完毕.请猜猜大小:')

    # 读取用户输入
    shuru = int(input('请输入骰子的大小(大输入2,小则输入1):'))

    # 判断用户的猜测是否正确  # 设定两个骰子的值，大于6等于大，否则就是小
    if ((q1 + q2) > 6 and shuru == 2) or ((q1 + q2) < 6 and shuru == 1):

        print('您猜对了,两个骰子分别为{}和{}'.format(q1, q2))
        print('恭喜{}!本局游戏获得2个游戏币'.format(username))
        # 奖励游戏币
        money += 2
    else:
        print('您猜错了,两个骰子分别为{}和{}'.format(q1, q2))
        print('很遗憾,本局游戏到此结束!!!')


# 判断用户是否要继续游戏

       while True :
           shuru = input('是否需要扣除2枚游戏币,重新开始游戏?(y/n)')
           if shuru == 'y' and money > 2:
               break
           elif shuru != 'y' or money < 2:
               print('退出游戏!!!!!!')
               exit()


