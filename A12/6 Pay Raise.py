def pay(sal):#its a one to one correspondence where wage is hourlyWage
    newSal= 0
    if sal>=40000:
        newSal= sal+2000+(.02*sal)
        return newSal

    if sal<40000:
       newSal= sal+ (.05*sal)
    return newSal




#main
name=input("Enter first and last name: ").title()
sal=eval(input("Enter annual salary: "))
earnings= pay(sal)


print("Earnings: ${0:,.2f}".format(earnings), "is", name +'s', " new salary for the next year.")
print("Your current salary is", "${0:,.2f}".format(sal))









