"""
11 - 

Date: 2022/12/15

"""
import random

print('*'*30)
print('欢迎进入澳门赌场')
print('*'*30)

username = input('请输入你的用户名:')
money = 0

# 判断用户是否进入游戏
while True:
    answer = input('确定进入游戏吗? (y/n)')
    if answer == 'y':
        break
    elif answer == 'n':
        print('退出游戏!!!!!')
        exit()

# 判断游戏币是否充足
while money < 2:
    n = int(input('金币不足,请充值(100块钱等于30个游戏币,充值必须是100的倍数)'))
    # 充值金额判断
    if n % 100 == 0 and n > 0:
        money = (n // 100) * 30

# 打印当前金币数量
print('当前游戏币是:{},玩一局游戏扣除游戏币2个'.format(money))

# 进入游戏
print('进入游戏.......')
while True:
    # 模拟骰子，产生骰子的值
    t1 = random.randint(1,6)
    t2 = random.randint(1,6)

    # 设定两个骰子的值，大于6等于大，否则就是小
    money -= 2 # 扣除金币
    print('您的金币余额为{}'.format(money))
    print('系统洗牌完毕,请猜大小:')

    # 读取用户输入
    guess = input('请输入大或者小(大,输入1,小,输入0):')



# 判断用户的猜测是否正确
    if ((t1 + t2) > 6 and guess == "1") or ((t1 + t2) < 6 and guess == "0"):
        print('您猜对了，两个骰子的值分别是{}和{}'.format(t1, t2))
        print('恭喜{}!本局游戏获得奖励1个游戏币.!!!'.format(username))

        # 奖励金币
        money += 1
    else:
        print('您猜错了，两个骰子的值分别是{}和{}'.format(t1, t2))
        print('很遗憾!本局游戏输了.....')

    # 判断用户是否继续游戏
    while True:
        answer = input('是否继续再来一局游戏,要扣除2枚游戏币?(y/n)')
        if answer == 'y' and money >= 2:
            break
        elif answer != 'y' or money < 2:
            print('退出游戏!!!!!')
            exit()
