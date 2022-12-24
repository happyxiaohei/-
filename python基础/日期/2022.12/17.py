"""
17 - 

Date: 2022/12/17

"""
# isalpha()  是否是字母   isdigit()  是否是数字

s = 'abcd'
result = s.isalpha()
print(result)

s = '3338888'
result = s .isdigit()
print(result)

sum = 0
i = 1

# while i<=3:
#     num = input('请输入数字:')
#
#     if num.isdigit():
#         num = int(num)
#         sum+=num
#         print('第{}个数字累加成功!'.format(i))
#         i+=1
#
#     else:
#         print('不是数字')
#
# print('sum=',sum)


#join()   '-'.join('abc')


new_str = '-'.join('abc')
print(new_str)

# python  列表    list = ['a','v','o','9']  数组

list1 = ['a','v','o','9']
result = ''.join(list1)
print(result)

result = '  '.join(list1)
print(result)
print(type(result))

#

s = '     hello    '

# s = s.lstrip()  # 去除字符串左侧的空格
#
# print(s+'8')
#
# s = s.rstrip()# 去除右侧的空格
#
# print(s+'8')

s = s.strip()
print(s+'8')


# split()  分割字符串 , 次数

s = 'hello world hello kitty'

result = s.split(' ')
print(result)

result = s.split(' ',2)   # 2表示按照空格作为分隔符,分割字符串2次
print(result)


n = s.count(' ')  # count (args) 求字符串中指定(args)中的个数
print('个数:',n)








































