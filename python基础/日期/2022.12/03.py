"""
03 - 赋值运算符

Date: 2022/12/3

"""
name = 'admin'

#将'admin'的值赋值给变量name

#1+1=2

name1 = name

print(id(name),name)
print(id(name1),name1)


name2 = name
print(id(name2),name2)

#  id()

name1 = 'admin1'

print(id(name),name)
print(id(name1),name1)

name = 'admin2'

print(id(name),name)

name3 = name

print(id(name3),name3)

# 扩展后的赋值符号   +=  -=  *= /=  ...

num = 8

num += 5   #  num = num + 5  此时+ 代表数学加号

num -= 10  # num = num - 10
print(num)

a = 'abc'

a += 'ff'   # 等价与:  a = a + 'ff'  此时'+'就是连接符号
            # 此时包含两个动作: 1. 连接 2.连接后的结果赋值

print(a)

# a -= 'kk'  # 这种情况下不支持
#
# print('a=',a)


'''
测试:

-= 
*=
/=
只是可以应用在数值,字符串不支持.
'''


# + - * /  算术运算符
#扩展的算术运算符: ** //

a = 8
b = 2

result = a * b
# print('乘法运算:'result)
#
# result = a / b
# print('除法运算:'result)
#
# b = 3
# result = a ** b # b = 2  8*8=64   8*8*8 = 512  a的b次幂
# print('乘法运算:'result)
#
# b = 2
# result = a // b  #整除  9/2 = 4.5   取整 :4
# print('除法运算:'result)

#
# result = a % b  # 9%2 = 1
# print('取余数运算:',result)
#






'''
总结:
print()输出
变量 常量
name='admin'
print (name)
name='jack'
print(name)
print(name,age)
print(values,...,sep = '',end='\n')

格式化的输出:
输出字符串:

1.占位符
%s  %d  %f  
pront('%s,%d,%f'%(value,value.value))
类型转换:
int --str
age = 18 -->'18'
str(age)-->'18'

str -->int
s = '18'
s = '18a'
int(s --->typerror



2.format
print('{},{}.....format())

input() 输入:阻塞式

name = input('  请输入姓名:')

 运算符:
 
 算数运算符:  + - * / % ** //
 
print('*'*50)
 
赋值运算符:

= += -= .............
name = 'jack'
name1 = 'jake'



'''


print('*' * 50)

print('\t 英雄联盟')

print('*'*50)














