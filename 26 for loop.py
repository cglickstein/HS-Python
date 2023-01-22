i = 2
while i < 6:
    print(i, i*i)
    i+=1 #keeps it from going forever
print ("The end")

#same thing
for i in range(2,7): #will only go to six like in a slice
    print(i, i*i)
print("The end again")
print (i) #you get 6 which is the last time it ran 9didnt change (expect for in print in the actaual for loop)



#Display population from 2014 to 2018
pop=30000
print("{0:10} {1}" .format("Year", "Population")) #spacing zerioth item, year, to have 10 characters and population which is 1

for year in range(2014,2019):
    print("{0:<10d} {1:,d}" .format(year,round(pop))) #< is left aligned and 10 is how many spaces. the year takes up 4 spaces, so there are 6 spaces left
    pop+=.03*pop

#STOP TURNS TO POTS
word= input("Enter a word: ")
reversedWord=""
for i in word: #goes through every single character, ch is made up variable name, ch changed to i
    reversedWord= i+reversedWord #s"" then adds t so ts"" then ends up being pots""
    print(reversedWord, end ='')
