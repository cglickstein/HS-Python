phrase= input("Enter a phrase: ")
phrase = phrase.lower()
count = 0
vowel = ["a", "e", "i", "o", "u"]
for character in phrase:
    if character == vowel[0] or character== vowel[1] or character == vowel[2] or character ==vowel [3] or character ==vowel[4]:
        count+=1

print(count)










