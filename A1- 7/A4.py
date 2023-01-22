#Income
rev=eval(input("Enter annual revenue"))
exp=eval(input("Enter annual expenses"))
netIncome= rev-exp
print("${0:,.2f}".format(netIncome)) #dont forget to specify whether float, digit, or number

#Present Value
f=eval(input("Enter future value"))
r=eval(input("Enter interest rate as percentage"))
n=eval(input("Enter number of years"))
presentValue= (f/((1+r/100)**n))
print("${0:,.2f}".format(presentValue)) #LEARN THIS

#Change In Salary
sal=eval(input("Enter salary"))
newSal=sal+sal*.05
newSal+=newSal*.05
newSal+=newSal*.05
print("New salary:",("${0:,.2f}".format(newSal)))
print("{0:,.2f}%".format(((newSal-sal)/sal)*100))


