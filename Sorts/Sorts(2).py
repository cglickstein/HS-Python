def main():
    #Custom sort a list of words
    list1=["democratic", "sequoia", "equals", "brrr", "break", "two"]
    list1.sort(key=len, reverse=True) #opposite order, longest to shortest
    print("Sorted by length in ascending order:")
    print(list1,'\n')


main()
