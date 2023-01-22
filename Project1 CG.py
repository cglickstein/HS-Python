#Collecting Input:
name=input("Enter buyer's first and last name: ")
name=name.title()
address=input("Enter buyer's street address (Ex. 1234 Smith Ave.): ")
address2=input("Enter buyer's city, state, and zip (in format:city,state zip Ex. Bensalem,PA 19020): ")
basePrice=eval(input("Enter the base price of the car: "))
taxOfCar=eval(input("Enter the tax of the car (as a percentage number Ex .05): "))
licenseFee=eval(input("Enter the license fee of the car (as a percentage number Ex .05): "))
dealerPrepCharge=187
destinationCharge=eval(input("Enter destination charge: "))
tradeinPrice=eval(input("Enter price for trade in: "))

#Invoice:
print( )
print("Your invoice is now printing")
print("Invoice")

#Invoice-Flip the Name
space=name.find(' ')
firstName=name[:space]
lastName=name[space+1:]
lastName=lastName+","
name=firstName+" "+lastName
nameBeforeReverse=name.split()
nameBeforeReverse.reverse()
joinedName=''.join(nameBeforeReverse)
print(joinedName)

# SIMPLER METHOD OF DOING THIS- name=input("Enter name")
#title=name.title()
#space=title.split(" ")
#print(space[1],",",space[0],)

#Invoice-Invoice Number
print(address)
print(address2)
lastNameLetters=lastName[:2]
lastNameLetters=lastNameLetters.upper()
space=address2.rfind(' ')
zip=address2[space+1:]
zipNumbers=zip[2:]
firstNameLetter=firstName[:1]
firstNameLetter=firstNameLetter.upper()
comma=address2.find(',')
cityLetter=address2[:1]
cityLetter=cityLetter.upper()
combination=(lastNameLetters,zipNumbers,cityLetter,firstNameLetter)
combination=''.join(combination)
print(combination)


#Numerical Calculations:
print( )

#Display Base Price
basePrice1=("${0:,.2f}".format(basePrice))  #:10?
print("Price of car:",basePrice1)

#Display Tax Price Of Car-percentage
taxOfCar1=("{0:,.2%}".format(taxOfCar)) #keep as deci?
print("Tax Percent:",taxOfCar1)

#Total Taxes Owed- CALCULATION
totalTaxesOwed=basePrice*taxOfCar
totalTaxesOwed1=("${0:,.2f}".format(totalTaxesOwed))
print("Total Taxes Owed:",totalTaxesOwed1)

#Display License Fee-percentage
licenseFee1=("{0:,.2%}".format(licenseFee))
print("License Fee Percent:",licenseFee1)


#Total License Fee Owed- CALCULATION
totalLicenseFeeOwed=basePrice*licenseFee
totalLicenseFeeOwed1=("${0:,.2f}".format(totalLicenseFeeOwed))
print("Total License Fee Owed:",totalLicenseFeeOwed1)


#Display Dealer Prep Charge
dealerPrepCharge1=("${0:,.2f}".format(dealerPrepCharge))
print("Dealer Prep Charge:",dealerPrepCharge1)

#Display Destination Charge
destinationCharge1=("${0:,.2f}".format(destinationCharge))
print("Destination Charge:",destinationCharge1)




#Final Price- CALCULATION2
finalPrice=basePrice+totalTaxesOwed+dealerPrepCharge+destinationCharge
finalPrice1=("${0:,.2f}".format(finalPrice))
print("Final Price:",finalPrice1)

#Display Trade-in Amount
tradeinPrice1=("${0:,.2f}".format(tradeinPrice))
print("Trade-in Amount:",tradeinPrice1)

#Total Bill- CALCULATION2
totalBill=finalPrice-tradeinPrice
totalBill=("${0:,.2f}".format(totalBill))
print("Total Bill:",totalBill)

print( )
print(input("Thank you for buying your car at Python Dealership!"))
