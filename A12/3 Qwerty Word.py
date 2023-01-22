def isQwerty(word):
    qwerty=('Q', 'W', 'E', 'R','T', 'Y', 'U','I', 'O', 'P')
    for i in word:
        if i not in qwerty:
            return False

        return True



word=input("Enter word to see if it is a Qwerty Word: ").upper()

if isQwerty(word): #bulyean, taking result from isVowelWord then not assigning but checking right away to see if true or false
    print(word.title(), "is a Qwerty Word.")
else:
    print(word.title(), "is not a Qwerty Word.")
