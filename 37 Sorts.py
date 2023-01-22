def main():
    #custom sort a list of words
    list1=["democratic", "sequoia", "equals", "brrr", "break", "Two"]
    list1.sort(key=len, reverse=True) #alphabetical sort? uppercase is lower #(reverse=True) does descending order
    #smallest length to greatest length
    print("Sorted by length in ascending order: ")
    print(list1, '\n')
    list1.sort(key=numberOfVowels, reverse=True) #send all words- special function that works only with key
    print("sorted by number of vowels in dese=cending order: ")
    print(list1, '\n')

    #list1.sort(key= lastCharacter)
    list1.sort(key=lambda x:x[-1]) #go through each thing in list is x
    print("sorter by last character in ascending order (because no reverse=True)")
    print(list1, '\n')

def lastCharacter(word):
    return word[-1]



def numberOfVowels (word): #knows to go through everything in list1
    vowels= ('a', 'e', 'i', 'o', 'u')
    total= 0
    for vowel in vowels:
        total+=word.count(vowel)
    return total

main()
