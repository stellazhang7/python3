#! /usr/bin/python3

str='Runoob'

print(str)
print(str[0:-1])  #从第一个到倒数第二个 不显示最后一个
print(str[-6]) #第一个 也是0
print(str[2:5]) #第三个到第六个 不显示第六个
print(str[2:]) #从第三个到最后
print(str * 10) #打印十次
print(str + '你好') #字符串拼接

print('-------------')

print('hello\nrunoob')  #转义字符\n 代表换行
print(r'hello\nrunoob') #raw 不处理后面的转义字符