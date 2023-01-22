word= input("Enter a word: ")
firstLetter= word[0]
vowel = ["a", "e", "i", "o", "u", "h", "y", "w",]


first = ''
for i in word.lower(): #.lower()
    if i != vowel[0] and i != vowel[1] and i != vowel[2] and i !=vowel [3] and i !=vowel[4] and i !=vowel[5] and i !=vowel[6] and i!=vowel[7]:
        #print(i)
        first= first+i

print("first:", first)

first=first.lower()
newerWord =first[0]
first=first[1:]

for i in range(len(first)):
    if first[i] == "b" or first[i]== "f" or first[i] =="p" or first[i]=="v": #can i do more things
        newerWord+="1"

    elif first[i] == "c" or i== "g" or i== "j" or i=="k" or i=="q" or i=="s" or i=="x" or i=="z":
        newerWord= newerWord + "2"

    elif first[i] == "d" or i== "t":
        newerWord= newerWord + "3"
    elif first[i] == "l":
        newerWord= newerWord + "4"
    elif first[i]== "m" or first[i]=="n":
        newerWord= newerWord + "5"
    elif first[i] =="r":
        newerWord= newerWord + "6"
    print(i)
print(newerWord)



