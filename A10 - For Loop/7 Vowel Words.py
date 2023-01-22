word = input ("Enter a word: ")
vowel = ["a", "e", "i", "o", "u"]


flag = True
for i in vowel:
    if not i in word:
        flag = False

if flag == True:
    print(word, "is a vowel word.")
else:
    print(word, "is not a vowel word.")

