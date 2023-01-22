def pay(wage, hours):#its a one to one correspondence where wage is hourlyWage
    if hours<=40:
        amount=wage*hours
    else:
        amount= (wage*40) + ((1.5)*wage*(hours-40))
    return amount #amount is assigned into earnings




#main
hourlyWage=eval(input("Enter the hourly wage: "))
hoursWorked=eval(input("Enter the number of hours worked: "))
earnings=pay(hourlyWage, hoursWorked) #hourlyWage in def is a totally different variable, just have same value when sending to def
print("Earnings: ${0:,.2f}".format(earnings))
