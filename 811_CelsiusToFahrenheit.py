# 接受一个输入到a 将它转换成整数后 根据公式算出华氏度再转换成字符串拼接输出

a = input("please input celsuis degree: ")
c = int(a)
print("fahrenheit is " + str(c * 1.8 + 32))