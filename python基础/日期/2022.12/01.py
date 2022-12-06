"""
01 -  格式化输出

Date: 2022/11/30

"""
name = '啊甘'
age = 26
clazz = 2022


msg = '''
个人信息简介：
我的名字 ： %s
今年%s岁
现在在%s班级
''' % (name, age, clazz)
print(msg)

# %s 中的s是代表str 字符串类型 这个内置函数，加百分号就是强制类型的转换
# 然而 %s  是str( )的一种简写
#
# digit 数字类型  %d  这是一种简写   函数名称是int
#
#  %f  float 小数点后面的为数， 而且是四舍五入的方式记录
salary = 8899.32895
print('我的薪水是：%.4f' % salary)

'''

约起来去楼上看电影，下订单：
movie = '大侦探皮卡丘 '
ticket = 45.9
count = 35


格式：
电影：xxxx
人数：xxxx
单价：xxxx
总票价：xxxx    (小数点后保留1位）


总票价的计算公式
总票价 = 票价 * 人数

'''

movie = '大侦探皮卡丘 '
ticket = 45.9
count = 35
toatl = ticket * count

# 写法1

print('.' * 30)
print('写法1')
dingdan = '''
约起来去楼上看电影的订单
电影名称：《 %s 》
人数：%d 人
单价: %.1f 元
总票价: %.1f 元
''' % (movie, count, ticket, toatl)
print(dingdan)


# 写法2
print('.' * 30)
print('写法2')
dingdan1 = '约起来去楼上看电影的订单\n 电影名称: 《 %s 》 \n 人数：%d人 \n 单价：%.1f 元 \n 总票价:%.1f 元'\
    % (movie, count, ticket, toatl)
print(dingdan1)
# 写法3
print('.' * 30)
print('写法3')
print('电影名称：《 %s 》 ' % movie)
print('人数：%d 人 ' % count)
print('单价: %.0f 元 ' % ticket)
print('总票价: %.1f 元 ' % toatl)

print('.' * 30)

# 字符串的格式化输出
# 方式：1、使用占位符 %s  %d  %f   2. format函数
# format是字符串中的函数。 使用方法是 ' '.format   此处的. 点是调用[] {} ()

age = 2
s = '已经上'
message = '乔治说：我今年{}岁了，{}幼儿园'.format(age, s)
print(message)


name = '乔治'
age = 3
hobby = '玩恐龙！'
money = 5.89

message = '{}今年{}岁,最喜欢{},有零花钱：{}'.format(name, age, hobby, money)
print(message)
