def main():
    #menu()
    colors=["blue", "purple", "yellow"]
    def menu():
        print("Options Menu:")
        print("1. Add a color to the list")
        print("2. View all colors in the list")
        print("3. View all colors in the list that begin with a letter")
        print("4. Remove a color")
        print("5. Exit")
        choice=input(eval("Please choose a number from the menu options: "))
        while choice>=1 and choice<=5:
            return choice
            print(choice)

        else:
            print("Pick again. This number was not an option.")
            choice=input(eval("Please choose a number from the menu options: "))
            print(choice)




main()
print("end")
