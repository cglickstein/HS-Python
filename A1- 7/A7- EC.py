#1 list to string
list=["Keep","Cool","But","Don't"]
print("Keep", "Cool", "But", "Don't...")
wordToList = input("Enter word to add to list: ")
list.append(wordToList)
print(list)
final = " ".join(list)
print(final)

#2
fakeTuple=[2,5,6,7,0]
print(fakeTuple)
print("Numbers in tuple:", len(fakeTuple))
print("Sum of numbers:", sum(fakeTuple))

#real tuple
#tuple= 0, 1, 2, 3, 4, 5, 6
#print(tuple)

#3
phoneNum=input("Enter a 10 digit phone number without slashes or spaces:")
areaCode=phoneNum[0:3]
middle=phoneNum[3:6]
last=phoneNum[6:]
listOfNums=[areaCode,"-",middle,"-",last]
print(listOfNums)
realString = " ".join(listOfNums)
print(realString)

#4
string="around-the-clock"
string=string.split("-")      #.sep('-')
newString = " ".join(string)
print("Work", newString[:])
 #didnt use - to know where anything is
