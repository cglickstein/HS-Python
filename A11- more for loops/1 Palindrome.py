words= input("Enter a word or phrase: ").lower()
#words= words.join('')
print(words)

newWord='' #should i do this?
for i in words:
    if i == ",":
        print(i)

    elif i == "!":
        print(i)

    elif i== "?":
        print(i)

    elif i== ".":
        print(i)

    elif i== " ":
        print(i)


    elif i == "'":
        print(i)

    else:
        newWord=newWord + i #wasnt any of the things above. make them equal

print(newWord)





reversedWord=""

for i in newWord:
    reversedWord= i+reversedWord
print(reversedWord)



if reversedWord== newWord:
    print(words, "is a palindrome.")
else:
    print(words, "is not a palindorme.") #how to put \" quotes?

