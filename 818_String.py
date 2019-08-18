Path = 'C:\\user\\stella' #\的转义字符是\\
print(Path)

a = 'Jack says, \"I\'m Jack\"' #引号的转义字符是\"
print(a)

#字符串格式化
print("My name is %s , I am %d years old, and I live in %s"\
      %('Stella', 18.5, "Wuhan"))
#format:%s is string, %d is number - int

print("My name is {}, I am {} years old, and I live in {}"\
      .format('Stella', 18.5, "Wuhan"))



#字符串内建函数
name = "stella"
print(name.capitalize())
print(name.count("s"))
print(name.endswith("a"))
print(name.startswith("S"))
print(name.index("ll"))

print("720".isdigit())
print(name.replace("te","et"))
