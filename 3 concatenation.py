#You can add vars for strings and make new vars of just strings
str1="good"
str3="Goodbye"
print(len(str3))
#Method- .upper to uppercase whole thing
print(str1.upper())
str1=str1.upper() #Only stores upper case if you store it (add to variable)
print(str1)
#you can change something someone writes to all upper or lower case and then compare and see what they wrote
print("good BYE".capitalize()) #Upper case JUST first letter
print("good bye".title()) #upper case letters starting each word
print("good bye".count)
print("gOod BYE".count("BY")) #has to be next to each other - B and Y are next to each other.
#More than one character has to be a slice
print("       gOod     Bye     ".strip()) #Only strips both sides and not middle strips
#Chain (methods)
numberOfGees="Good Doggie".upper().count('G') #Dont chain more than three things togther
print(numberOfGees)

