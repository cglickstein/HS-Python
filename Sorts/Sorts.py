def main():
    #Custom sort a list of words
    list1=["democratic", "sequoia", "equals", "brrr", "break", "two"]
    list1.sort(key=len)#sorts by length of each word
    print("Sorted by length in ascending order:")
    print(list1,'\n')


main()
