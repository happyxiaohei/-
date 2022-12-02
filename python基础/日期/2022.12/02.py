"""
02 - 

Date: 2022/12/2

"""
# 输入 ： inprut ()

# name = input()

# print(name)
#
# name = input('请输入名字：')  #阻塞式
#
# print (name)


'''
练习：
游戏：捕鱼达人

输入参与游戏者用户名：
输入密码：

充值 ： 500

'''


username = input('输入参与游戏者用户名：')
password = input('请输入密码：')

print('%s请充值才能开始游戏！'%username)

coins = input('请充值：') # input键盘输入的都是字符串类型  即使输入的是500，
                        #它也会添加‘500’

coins = int(coins)

print('%s充值成功！当前游戏币是：%d'%(username,coins))

