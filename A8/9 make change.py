pounds= eval(input("Please enter the amount of pounds of apples: "))
cash= eval(input("Please enter the amount of cash given: "))
owe=pounds *2.50

cash= round(cash,2)
owe= round(owe,2)

if cash>owe:
    change= cash-owe
    print("Your change is","{0:,.2f}$".format(change))
elif owe>cash:
    due= owe-cash
    print("You owe", "{0:,.2f}$".format(due),"more.")

elif cash== owe:
    print("Thank you for the exact change. Have a nice day!")
