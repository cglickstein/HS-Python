#You cant change tuples. Tuples are immutable

#You can take a slice that's bigger than what you're printing really is, but you can't take an index that doesn't exist

t=(5,7,6,2) #dont need parenthesis
print(t)
print(len(t)),max(t),min(t),sum(t)
print(t[0],t[-1],t[:2]) #prints with parenthesis WHY
x,y,z=5,6,7
print(x) #corresponds to variables

#Nested List
regions=[("Northeast",55.3),("Midwest",66.9),("South",114.6),("West",71.9)] #List with tuples inside
#Now you can git rid of tuples because they are inside of a list, but you can't go inside and change population because it's in the
#tuple
print("The 2010 Population of the")
print(regions[1][0]) #one it gets tuple then it chooses 0 within the tuple
print("was")
print(regions[1][1])

totalPop=regions[0][1]+regions[1][1]
regions[2][1]+regions[3][1]
print("2010 total population", totalPop)
