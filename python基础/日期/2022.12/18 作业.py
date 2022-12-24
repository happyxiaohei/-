"""
18 作业 - 

Date: 2022/12/17

# """
# #方法1
#
# s1 = input('请输入第一个字符串:')
# s2 = input('请输入第一个字符串:')
# s3 = ''
# for i in s1:
#     # print(i,end = '')
#     if i not in  s2 :
#         s3 += i
#
# print(s3)
#
# s1 = s3
# print(s1)
#
# # 方法2
# for i in s2 :
#     s1 = s1.replace(i,'')
#     print(s1)
#
#
#
# #方法3
# for i in s2:
#     if i not  in s3 :
#         s3+=i
#
# print(s3)
#
# for i in s3:
#     s1 = s1.replace(i,'')
#
# print(s1)
#




'''
第二个作业
'''

# word = input('请输入单词:')
#
# for i in range(len(word)):  # 循环单词长度的次数
#
#     if word[i] <'A' or word[i]>'Z':
#         print('不喜欢,不是大写的')
#         break
#
#
#     else:
#         if i <len(word) -1 and word[i]==word[i+1]:
#             print('不喜欢,是叠词')
#             break
#
# else:
#     print('喜欢!')


'''
第三个作业
'''
s = ''
while True:
    username = input('请输入用户名;')
    password = input('请输入密码:')
    email = input('请输入邮箱:')

    username = username[0:20]
    password = password[0:20]
    email = email[0:20]

    msg = '{}\t{}\t{}\n'.format(username,password,email)

    msg = msg.expandtabs()
    s += msg
    if username == 'q'or username == 'Q' or password == 'q'or password == 'Q' or email == 'q'or email == 'Q':
        break

print(s)











































