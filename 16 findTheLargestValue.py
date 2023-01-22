#Find the largest of 3 numbers
#Input the 3 numbers
firstNumber=(eval(input("Enter the first number: ")))
secondNumber=(eval(input("Enter the second number: ")))
thirdNumber=(eval(input("Enter the third number: ")))
#Determine and display the largest value
max=firstNumber
if secondNumber>max:
    max=secondNumber

if thirdNumber>max:
    max=thirdNumber

print("The largest numer is",max,".")
print("The largest number is"+str(max)+".")
print("The largest number is",str(max)+".")

#.sort()
