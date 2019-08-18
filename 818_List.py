#List内建方法
list = [1,2,3]
print(len(list)) #list长度
print(max(list)) #list里最大的
print(min(list)) #最小

list.append("4") #列表末尾添加新对象
print(list)

print(list.count(4))

list.insert(0, 7) #第一位是插入位置，第二个是插入值
print(list)

list.pop() #去掉最后一个元素
print(list)

list.remove(7)
print(list)

list.reverse()
print(list)

list.sort(reverse= True) #倒序排列，默认为false
print(list)

list.clear()
print(list)
