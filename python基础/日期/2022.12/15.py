"""
15 - 查找相关的,替换

Date: 2022/12/16

"""

# find() rfind() lfind() index() rindex() replace()

s1 = 'index lucy lucky goofs'

result = 'R' in s1
print(result)

position = s1 .find('R')  # 返回值是-1 则代表没有找到

print(position)

position = s1 .find('l')  # 如果可以找到则返回字母第一次出现的位置
print(position)


# find('要查找的字符',start,end)
p = s1 .find('o',position+1,len(s1)-5)   # 也可以指定开始位置查找
print(p)

ur1 = 'https;//www,baidu.com/img/bd_logo1.png'

p = ur1.rfind('/')  #right find 从右侧检索/的位置
print(p)

filename = ur1[p+1:]
print(filename)

p = ur1.rfind('.')
kz = ur1[p+1:]
print(kz)


# 替换

s1 = 'index lucy lucky goofs'

 # replace(old,new,[max]) (旧的,新的,[替换次数])
s2 = s1.replace(' ','#')
print(s2)

s2 = s1.replace(' ','')
print(s2)






















