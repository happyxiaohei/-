"""
13 -

Date: 2022/12/15

"""
# # s1 = "123"
# # s2 = '123'
# # s3 = '''
# # 123'''
# # print(id(s1), id(s2), id(s3))
#
# # in  在,,,,里面
#
# name = 'steven'
#
# result = 'tv' in name  #返回值是布尔类型 True   False
#
# print(result)
#
#
# # nut in    没有在,,,,里面
#
# result = 'tv' not in name    #返回值是布尔类型 True   False
# print(result)
#
# #  % 字符串的格式化
#
# print('%s说:%s'%(name,'大家好好学习'))
#
# #  r 保留原格式    有r  则不发生转义  没有r则发生转义(例如:\')
#
# print(r'%s说:\'哈哈!\''% name)
#
#
# #  [ ]   [  :  ]
#
# filename = 'picture.png'
#
#
# # 位置都是从0开始,位置也会称作下标或者索引
# print(filename[5])   # 通过[]可以结合位置 获取字母  特点 : 只能获取一个字母
#
# # range (1,10) ----> [1:10]
#
# print(filename[0:7])  #包前不包后面
#
# print(filename[3:7])  # 截取字符串
#
# #  省略
# print(filename[3:])   #只要省略的是后面的,表示一直取到字的末尾
# print(filename[:7])   #只要省略的是前面的,表示从0开始取值
#
# #负数
# print(filename[8:-1])
#
# # [ : :-1]   倒叙
# print(filename[::-1])
#
# str1 = 'abcdefg'
# print(str1[-1:-6:-1])
#
# print(str1[0:5:-1])
#



'''
str[start:end:方向和步长]
方向:   1  表示从左向右
        -1 表示从右向左
        注意数值的顺序
        比如:  正向: 5:0 就不行了
              反向:5:0  就可以取值了
'''




#练习:   hello world
#逆序输出world
#正向输出hello
#逆序输出整个 hello world
#打印获取 oll
#打印llo wo


str12 = 'hello world '

print(str12[-1:-7:-1],'----1')
print(str12[:5],'---2')
print(str12[::-1],'----3')
print(str12[4:1:-1],'----4')
print(str12[2:-3],'----5')

#
print(str12[::-3])





