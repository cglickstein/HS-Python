#Analyze a sentence
'''sent=input("Enter a sentence")
words=sent.split()
print(len(words))

#2 Analyze a sentence
sent=input("Enter a sentence")
space=sent.find(' ')
firstWord=sent[:space]
space2=sent.rfind(' ')
lastWord=sent[space2+1:]
print(firstWord)
lastWord=lastWord[:-1]
print(lastWord)



#2
name=input("Enter name: ")
#lowercase=name.lower()
title=name.title()
space=title.split(" ")
print(space[1],",",space[0],)'''



#3 Name
name=input("Enter first and last name: ").title()
space=name.find(' ')
#firstName=name[:space]
#lastName=name[space+1:]
space=name.split(" ")
print(space[1]+","+ " " +space[0])


#4 Name
threePartName=input("Enter a three part name: ").title()
space=threePartName.find(' ')
name1=threePartName[:space]
spaceTwo= threePartName.rfind(' ')
name2=threePartName[space+1:spaceTwo]
print(name2)
#print(middleName)

