#find the minimum, maximum, and average of a sequence of numbers
#obtain a list of numbers
list1=[]
print("Enter -1 to terminate entering numbers")
num=eval(input("Enter a non-negative  number: "))
while num !=-1:
    list1.append(num)
    num=eval(input("Enter a non-negative number: ")) #keeps appending numbers that aren't negative to the list

if len(list1)>0:
    list1.sort()
    print("minimum",list1[0])
    print("maximum",list1[-1])
    print("average",sum(list1)/len(list1))
else:
    print("No non- negative numbers: ")
