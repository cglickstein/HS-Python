balance= 1000

print("Options Menu:")
print("1. Make a Deposit")
print("2. Make a Withdrawal")
print("3. Obtain Balance")
print("4. Quit")
option=""

while option!="4":
    option=input("Please enter a number option from the menu above: ")
    if option=="1":
        deposit =eval(input("Enter Deposit: "))
        balance+= deposit

    elif option=="2":
        withdrawal =eval(input("Enter Withdrawal: "))
        if withdrawal > balance:
            print("Withdrawal denied. Withdraw cannot exceed 1,500$")
        else:
            balance-= deposit #continue before but didnt know why i need this

    elif option=="3":
        print("${0:10,.2f}".format(balance), "is your current balance.")



#OBTAIN BALANCE three= print ("balnce obtained is", balance)
# QUIT print that if you enter -1 it will terminate then while num != -1
