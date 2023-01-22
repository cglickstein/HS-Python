print("hello", "World") #By default, sep is a space
print("hello", "World","Today", sep="**")

print("HELLO") #By default end is an enter
print("WORLD")
print("Today is", end=" ")
print("WORLD!")

#ESCAPE SEQUENCE (tab is 6 spaces)
print("0123456789")
print("abc")
print("a\tb\tc") #\t is one character that means tab
#escape sequence always has to be inside quotes
print(len("a\tb\tc")) #5 characters

print("hello", "World","Today", sep="\t")
 #.expandtabs(2) - makes 2 spaces


#\n means new line
print("a\nb\nc")
print()

print('say it ain\'t so') #make something a character like quotes
print("he said, \"yes\"")
print("\\")

