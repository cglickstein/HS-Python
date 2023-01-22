list=['a','b','c','d']
list[0]=list[0].upper()
print(list)
#you can start off with if and have a condition... then ends in if

#Determine the larger of two numbers
#obtain the numbers from the user
num1=eval(input("Enter the first number: "))
num2=eval(input("Enter the second number: "))
#Determine and display the larger value
if num1> num2:
    print("The larger value is", str(num1)+ ".")
elif num2>num1:
    print("The larger value is", str(num2)+ ".")
    #else is that everything goes into it but elif can have many conditions and doesnt include everything- MORE THAN I CONDITION
else:
    print("The two numbers are equal")
