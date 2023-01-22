#8 Pig latin
word=input("Enter a word: ").lower()
beginningOfWord=word[0]
sL = word[1]
tL= word[2]
fL= word[3]
fiL= word[4]

if beginningOfWord == "a" or beginningOfWord.startswith("e") or beginningOfWord.startswith("i") or beginningOfWord.startswith("o")\
    or beginningOfWord.startswith("u"):

    print(word+"ay")

elif sL == "a" or sL.startswith("e") or sL.startswith("i") or sL.startswith("o")\
    or sL.startswith("u"):
    start=word[0]
    rest=word[1:]
    print(rest+start+"ay")

elif tL == "a" or tL.startswith("e") or tL.startswith("i") or tL.startswith("o")\
    or tL.startswith("u"):
    start=word[:2]
    rest=word[2:]
    print(rest+start+"ay")

elif fL == "a" or fL.startswith("e") or fL.startswith("i") or fL.startswith("o")\
    or fL.startswith("u"):
    start=word[:3]
    rest=word[3:]
    print(rest+start+"ay")

elif fiL == "a" or fiL.startswith("e") or fiL.startswith("i") or fiL.startswith("o")\
    or fiL.startswith("u"):

    start=word[:3]
    rest=word[4:]
    print(rest+start+"ay")



