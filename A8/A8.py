'''#1 Tip
check=eval(input("Enter bill on check: "))
tip=check*.15
minimumTip=2
if tip<minimumTip: #dont forget the :
    print("Tip should be more than 2$")
else:
    print(tip,"$")

#2
bagelsOrdered=eval(input("Enter amount of bagels ordered"))
if bagelsOrdered<6:
    print(bagelsOrdered*.75,"$")
else:
    print(bagelsOrdered*.60,"$")


#3
widgets=eval(input("Enter amount of widgets ordered"))
if widgets<100:
    print(widgets*.25,"$")
else:
    print(widgets*.20,"$")


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

#5 Quiz
q=input("Who is the mother of Bais Yaakov? ").title()
if "Sarah Schenirer":
    print("You are correct")

else:
    print("Nice try")

#6 Overtime Pay
hours= eval(input("Enter number of hours worked this week: "))
wage= eval(input("Enter hourly wage: "))
if hours>40:
    fortyHours=40
    fortyHours=fortyHours*wage
    moreHours=fortyHours-40
    moreHours=moreHours*(wage+(wage*.5))
    print("{0:10.2f}".format(moreHours) + "$")

else:
    print("{0:10.2f}".format (hours*wage)+"$")'''

    #7 Compute an average
score1=eval(input("Enter the 1st score: "))
score2=eval(input("Enter the 2nd score: "))
score3=eval(input("Enter the 3rd score: "))
m = score1
if score2<m:
    m = score2
if score3<m:
    m=score3
lON= [score1, score2, score3]
lON.remove(m) #Dont do variable equals variable.remove
a = (lON[0] + lON[1])/2
print(a)



    #find which is highest then next highest






