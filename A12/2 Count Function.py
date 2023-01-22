def getCount(word):
    amount= 0
    for i in word:
        if i == letter:
            amount+=1
    return amount





word=input("Enter the word: ").lower()
letter= input("Enter the character you wish to count in the word: ").lower()
amount= getCount(word)

print("The word", word, "contains", amount, letter +"'s.")
