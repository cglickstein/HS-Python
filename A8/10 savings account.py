balance=eval(input("Please enter current balance: "))
withdrawal= eval(input("Please enter the amount you would like to withdrawal: "))
newBal= balance-withdrawal

if newBal> balance:
    newBal="{0:,.2f}$".format(newBal)
    print("Balance:", newBal,"WITHDRAWAL DENIED")
elif newBal<150:
    newBal="{0:,.2f}$".format(newBal)
    print("Balance:", newBal,"Sorry, balance is below 150$")

else:
    newBal="{0:,.2f}$".format(newBal)
    print("Your current balance is now", newBal)
