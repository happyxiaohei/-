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

#
# username = input('输入参与游戏者用户名：')
# password = input('请输入密码：')
#
# print('%s请充值才能开始游戏！'%username)
#
# coins = input('请充值：') # input键盘输入的都是字符串类型  即使输入的是500，
#                         #它也会添加‘500’
#
# coins = int(coins)
#
# print('%s充值成功！当前游戏币是：%d'%(username,coins))

# 练习


'''
游戏： 英雄联盟
角色：xxx
拥有的装备：xxx
购买装备：xxx
付款金额：xxx

xxx拥有xxxx装备，花了xxx钱
'''
# 写法1

# print('''
# ***********
#   英雄联盟
# ***********
# ''')
# game = "英雄联盟"
# role = input('请输入角色名称')
# print('%s请购买装备后才能开始游戏!'%role)
# buy = input('请输入购买的装备名称：')
# money = input('请付款：')
# money1 = int(money)
# print ('%s购买成功！'%buy)
# print('恭喜玩家{}在英雄联盟游戏中消费{}元，拥有了{}武器。'.format(role, money1, buy))


# 写法2
print('''
***********
  英雄联盟
***********
''')
role = input('请输入角色名称:')
equipment = input('请输入拥有的装备:')
upgrade_eqipment = input('输入想购买的装备:')
pay = input('输入付款金额:')

# 变量的赋值替换

equipment = upgrade_eqipment

print('{}拥有{}装备,购买此装备花了{}元'.format(role, equipment, pay))
