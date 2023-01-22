word = input("Enter a word: ") #cat
newWord= word[1:] #at
previous =word[0] #c
flag = True

for letter in newWord: #c
    if letter <= previous: #a

        flag = False
    previous = letter

if flag == True:
    print (word, "is in alphabetical order.")
else:
    print(word, 'is not in alphabetical order.')


