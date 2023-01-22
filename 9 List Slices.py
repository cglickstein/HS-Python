team=["Seahawks",2014,"CenturyLink Field"]
print(team[0])
print(team[1:2]) #making list of list. Since slice, doesn't print out the 2
print(team[1:3])
print(team[:])
print(team[1:])#or [:3]
print(team[-1]) #prints last thing
list1=['a','b','c','d','e','f']
#length is 6 because starts at 1 (Index starts at 0) OR
print(list1[2:6])
#start c  end (inlude f)
print(list1[2:5])

list2=list1[2:len(list1)] #2 is before the 'c'
print(list2)

print( )

myList="a**b**c".split('**') #figures out if string is connected with spaces or enters (\n)
print(myList)

line=["To","be","or","not","to","be"]
print(" ".join(line)) #attaches dif things to make a string

krispies= ["Snap","Crackle","Pop"]
print(", ".join(krispies))

