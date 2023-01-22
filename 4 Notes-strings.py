#concatenate- puts strings together instead of adding them
print("ha"*4)
print("cha-"*2+"cha") #c
print("a"+"b")
print(1+2)
print("1"+"2")
town=input("Enter the city that you live in: ")
print(town)
age=input("Enter your age: ")
age=eval(age) #turns into integer(not .0) or int or float(keeps .5)
#You can't add string and input
#inputs will always be a string
print("In 2 years you will be", age+2) #put comma not plus because can't concatenate. Have to turn into integer first.
age2=eval(input("Enter your friend's age: ")) #or eval
print(age2+12)
