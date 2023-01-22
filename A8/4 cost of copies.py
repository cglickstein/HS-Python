#4 Cost of coppies
copies=eval(input("Enter amount of copies: "))
hundred=100
if copies>100:
    cheaper=copies-hundred
    cheaper=cheaper*.03
    expensive=hundred*.05
    finalPrice=cheaper+expensive
    print("{0:10.2f}".format(finalPrice)+"$")
else:
    print("{0:10.2f}".format(copies*.05)+"$")
