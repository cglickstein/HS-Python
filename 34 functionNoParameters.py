def main():
    #extract first name from full name
    fullName=input("Enter a person's full name: ")
    print("First Name:", firstName(fullName)) #if it didn't return anything then there would be nothing to print. returns to print

def firstName(fullName):
    firstspace=fullName.index(" ")
    givenName= fullName[:firstspace]
    return givenName



main() #1st item running
print("end")
#the whole thing ends here

#DONT PASS VARIABLE BUT VALUE OF VARIABLE
#SCOPE- VARIABLE WORKS WITHIN A SCOPE OF CODE (VAR INSIDE IF STATEMENT OR CREATED WITHIN BLOCK)
