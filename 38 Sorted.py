list1=["estie","green","loves","her","sleep"]
list2=sorted(list1)
print(list2)
list3=["red","white","blue"]
list3.sort()
print(list3)
list4=sorted("spam") #breaks a string into a list
print(list4)
list5=sorted(list3,key=len) #remember, length is from least to greatest
print(list5)
