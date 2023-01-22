def isVowelWord(word):
    word=word.upper()
    vowels=('A', 'E', 'I', 'O','U')
    for vowel in vowels:
        if vowel not in word:
            return False
        return True
#ig goes through whole thing then it retunrs true, but false wouldnt bother checking anything else







word=input("Enter word: ")
if isVowelWord(word): #bulyean, taking result from isVowelWord then not assigning but checking right away to see if true or false
    print(word.title(), ":contains every vowel.")
else:
    print(word.title(), "does not contain every vowel.")
