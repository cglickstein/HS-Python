num1 = eval(input("Enter the 1st number: "))
num2 = eval(input("Enter the 2nd number: "))
num3 = eval(input("Enter the 3rd number: "))

list= [num1,num2,num3]

#for i in range (1,4):

for num in list:
    if num1 > num2 and num1> num3:
        highest = num1
    elif num2 > num1 and num2 > num3:
        highest = num2

    elif num3 > num1 and num3 > num2:
        highest = num3

print(highest)
