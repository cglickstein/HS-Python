def main():
    #Custom sort a list of words
    list1=["democratic", "sequoia", "equals", "brrr", "break", "two"]
    list1.sort(key=len)#sorts by length of each word
    print("Sorted by length in ascending order:")
    print(list1,'\n')
    list1.sort(key=numberOfVowels, reverse=True) #number of vowels does not have parenthesis even though going to a function
    print("Sorted by number of vowels in descending order:")
    print(list1,'\n')
    list1.sort(key=lastCharacter)
    print("Sorted by last character in ascending order:")
    print(list1,'\n')

def lastCharacter(abc):
    return abc[-1]

def numberOfVowels(word): #sending each word in the list
    vowels=('a','e','i','o','u')
    total=0
    for vowel in vowels:
        total+=word.count(vowel) #vowel is showing numbers of vowels in each word of the list
    return total

main()
