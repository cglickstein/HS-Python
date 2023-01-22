''''phoneNum = input("Enter a ten digit phone number: ")
123-456-7869
dash1= phoneNum[3]
#dash1= str(dash1)
print (dash1)
dash2 = phoneNum[7]
#dash2= str(dash2)

for i in phoneNum:
    phoneNum = list(phoneNum)
    print(phoneNum)
    if i == dash1:
        phoneNum = phoneNum. remove(dash1) #.remove is only for a list? #index might be changed once remove first dash
    if i == dash2:
        phoneNum = phoneNum.remove (dash2)
print(phoneNum)'''


phoneNum = input("Enter a ten digit phone number: ")
for i in phoneNum:
    if i != "-":
        print(i, end= '')


