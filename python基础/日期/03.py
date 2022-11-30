"""
03 - 

Date: 2022/11/30

"""
# %s 是一个占位符 ，这个占位符是属于格式化输出 ： %s  %d  %f


#

name = '啊甘'
age = 18
clazz = 'python2022'


adf = '''
个人信息简介：
姓名 ： %s
年龄 ： %s
班级 ： %s

'''%(name,age,clazz)

print (adf)





msg = '''
个人信息简介：
我的名字 ： %s
今年%s岁
现在在%s班级
'''%(name,age,clazz)
print(msg)

# %s 中的s是代表str 这个内置函数，加百分号就是强制类型的转换
# 然而 %s  是str( )的一种简写

# digit 数字类型  %d  这是一种简写



