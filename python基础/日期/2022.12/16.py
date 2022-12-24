"""
16 -  字符串内建函数

Date: 2022/12/16

"""

# encode 编码  decode  解码

# 编码:  网络应用的时候应用(中文一般会涉及编码问题)


msg = '认真上课!!!'

# https://www.baidu.com/s?wd=%E4%BB%8A%E6%97%A5%E6%96%B0%E9%B2%9C%E4%BA%8B&tn=SE_Pclogo_6ysd4c7a&sa=ire_dl_gh_logo&rsv_dl=igh_logo_pc


result = msg.encode('utf-8')

print(result)

# 解码

m = result.decode('utf-8')
print(m)



# startswith()   endswith ()   返回值都是布尔类型    True    False

#startswith()判断是否是以xxx开头的 ,endswith ()判断是否是以xxx结尾的

# 文件上传

#应用:文件上传 只能上传图片(jpg,png,bmp,gif)

filename = '笔记.doc'

r = filename.endswith('txt')  # filename是否是以txt结尾的

print(r)

s = 'hello'

result = s.startswith('he')

print(result)


#应用:文件上传 只能上传图片(jpg,png,bmp,gif)

path = input('请选择文件:') #C:\Users\Admin\mintty.asdf.png

#分析上传的文件路径

p = path.rfind('\\')
filename = path[p+1:]  #通过切片截取出文件名

#判断是否是图片类型?

if filename.endswith('png')or filename.endswith('jpg') :
    print('图片允许上传')
else:
    print('不是图片格式,只能上传图片')




while True:
    # 应用:文件上传 只能上传图片(jpg,png,bmp,gif)

    path = input('请选择文件:')  # C:\Users\Admin\mintty.asdf.png

    # 分析上传的文件路径

    p = path.rfind('\\')
    filename = path[p + 1:]  # 通过切片截取出文件名

    # 判断是否是图片类型?

    if filename.endswith('png') or filename.endswith('txt'):
        print('图片允许上传')
        break
    else:
        print('不是图片格式,只能上传图片')
























