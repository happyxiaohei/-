"""
04 - 比较运算符

Date: 2022/12/6

"""

# n1 = int(input('请输入第一个数:'))
#
# n2 = int(input('请输入第一个数:'))
#
# # 判断 n1 与 n2
#
# result = n1 > n2
#
#
#
# print('n1>n2',result)
#
# m1 = 'hello'
#
# m2 = 'hello'
#
# result = m1 == m2
#
# print('m1==m2',result)
#
# username = input('请输入用户名:')
#
# uname = 'admin123'
#
# # result = username==uname
# #
# # print('用户名的验证结果是:',result)
#
# result = username != uname
# #如果两者不相等则会返回true,相等则返回false
#
# print('用户名的验证结果是:',result)


# is 用户对象的比较  id 查看内存地址函数

age = 20

age1 = 20
print(id(age))
print(id(age1))

print(age is age1)

money = 2000000

# salary = 600000

salary = 2000000

print(id(money))
print(id(salary))
print(money is salary)

'''

数值is比较

小整数对象池
python 对小整数的定义是[-5,256] 这些整数对象是提前建立号的,不会被垃圾回收

大整数对象池:
终端是每执行一次,所以每次的大整数都重新创建

而在pycharm中,每次运行是所有代码都加载在内存中,属于一个整体

'''

'''
and or not

and  逻辑与
or  逻辑或
not 逻辑非

逻辑运算符的运算结果也是返回 true  false

true  and true  --->true  其他情况
true  and false -->false
false and true  --->false
false  and false --> false


8>10  and  6<8

false and true --->false

'admin ' == 'admin123'and '123456' == '12345' --->false
      false                     true



'''

n1 = 8
n2 = 5
n3 = 3
result = n1 >= (n2 + n3) and n1 > n2

print(result)

'''
步骤:
1. n1>=(n2+n3)  8 >= 8  true
2. n1>n2 8>5  true
3.true and true
4. 结果:true
'''

n2 = n2 + n3
# n2 --->8
result = n1 >= n2 and n1 == n3
#           true and false  ----> false
# 在and 运算符中  只要有一方的值是假(false)  那么结果就是假(false)
print(result)

n4 = (n1 + n3) - n2
# (8+3)-8=3  n4 = 3
result = n4 < n1 and (n4 + n3) > n2
# true  and false
# 那么结果为false (假)


'''
or : 或者
只要一边为真(true),结果即为真(true)

true or true   ----> true
true or false   ----> true
false or true   ----> true
false or false   ----> false

'''


