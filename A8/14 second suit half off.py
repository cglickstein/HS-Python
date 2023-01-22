firstSuit= eval(input("Please enter the price of the first suit: "))
secondSuit= eval(input("Please enter the price of the second suit: "))
if firstSuit> secondSuit:
    lower=secondSuit
else:
    lower= firstSuit
newCost= firstSuit + (.5*lower)
print("You owe", "{0:,.2f}$".format(newCost))
