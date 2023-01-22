list1=["two", "equals", "sequoia", "break", "brrr"]
list2=sorted(list1, reverse=True)#list 1 doesn't change
print(list1)
print(list2)
list3=["red", "white", "blue"]
list3.sort()
print(list3)
list4=sorted("spam")
print(list4)
list5=sorted(list3, key=len)
print(list5)
