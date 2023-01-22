var="9"
print(var.isdigit()) #12.54 wont work or 90- 90
var1="abc, edf"
print(var1.isalpha()) #cant do abc123
age= input ("Enter your age: ")
if age.isdigit():
    age=int(age)

else:
    print("Enter an age using numbers")


#print(age.isalnum()) can be number or alphabet or both- any character that is not a num or alpha will make it false (false, subtraction sign etc)

serial=input("Enter serial number")
if serial[0] .isdigit() and serial[1] .isalpha() and serial[2] .isanum():
    print('Good serial number')
else: print("Invalid serial number. Have caller give you a different number")



print(var1.islower())#just looks at letters, and you can have a bunch of characters that aren't letters

var2= " "
print(var2.isspace())




#Weather forecast light on top of Boston's
#John Hancock building
#steady blue, clear blue
#steady red, rain ahead
#flashing red, snow instead

color=input("Enter color: ")
mode=input("Enter mode: ")
if (color.lower()=="blue" and mode.upper()=="STEADY"):
    print("clear")

elif (color.lower()=="blue")and (mode.upper()=="FLASHING"):
    print("clouds")

elif ((color.lower()=="red")and (mode.upper()=="STEADY")):
    print("rain")

elif ((color.lower()=="red")and (mode.upper()=="FLASHING")):
    print("snow")

else:
    print("Incorrect color or mode")


print(not(color=="blue")) #not not true



#bulyan variables- always either true or false
flag=True #or False
var="fantastic"

if var.startswith("fan"):
    print("true part")
else:
    print("false part")

#easy to use if not function instead of not
#and, or
#age= , age= , age= and so on

#.endswith()

var2=22
print(var2.isdigit())

age=input("Enter Age: ")
if (age.isdigit()):
    age=int(age)


else: 
    print("Start over. You must enter a number")
