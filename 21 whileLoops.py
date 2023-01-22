#Loops have a condition just like our if statements- has to equal true or false. true goes through loops and false leaves.
num= 1
while num<=5:
    print(num)
    num+=1 #num= num+1
#keeps going until it doesn't apply anymore. You need a condition and something to check code.
print("The end") #if indent then it's part of the loop, so it runs with loop every time

serial=input("Enter serial number: ")
while serial.isdigit():
    print("serial only contains letters")
    serial=input("Enter serial number: ")
print("Thanks for the serial number. It is", serial)
#repeats forever if it keeps fulfilling statement because you never change or add anything to the varibale to keep being changed every time

numm=1
while numm <=5:
    numm+=1
    print(num)

print("num is now", numm)

numm=1
while numm <=5:
    print(num)
    numm+=1 #order makes a difference because print isn't a part of the loop #num =222

print("num is now", numm)
