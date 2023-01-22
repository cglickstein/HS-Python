'''
#1 Make Change
startingChange=eval(input("Enter the amount of change"))
quarter=startingChange//25
startingChange=startingChange-quarter*25
dime=startingChange//10
startingChange=startingChange-dime*10
nickel=startingChange//5
startingChange=startingChange-nickel*5
cents= startingChange//1
print("Quarters:",quarter,"Dimes:", dime, "Nickels:",nickel, "Cents:",cents)

#2 Unit Price
price=eval(input("Enter price of item"))
pounds=eval(input("Enter weight of item in pounds"))
oz=eval(input("Enter weight if item in ounces"))
totalOunces=oz+pounds*16
print("$",round(price/totalOunces,2))
'''
#3 Stock Portfolio
spy=eval(input("Enter amount invested in SPY: "))
qqq=eval(input("Enter amount invested in QQQ: "))
eem=eval(input("Enter amount invested in EEM: "))
vxx=eval(input("Enter amount invested in VXX: "))
total=spy+qqq+eem+vxx


print("ETF".ljust(5), "PERCENTAGE".ljust(10))
spyP="{0:,.2f}%".format((spy/total) *100)
print("SPY:",spyP.ljust(10))
qqqP="{0:,.2f}%".format((qqq/total) *100)
print("QQQ:", qqqP.ljust(10))
eemP="{0:,.2f}%".format((eem/total) *100)
print("EEM:", eemP.ljust(10))
vxxP="{0:,.2f}%".format((vxx/total) *100)
print("VXX:", vxxP.ljust(10))


total=("{0:10,.2f}$".format(total))
print( )
print("TOTAL AMOUNT INVESTED: ", total)
