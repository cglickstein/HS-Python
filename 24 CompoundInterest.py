#calculate the number of years to become a millionaire
numberOfYears=0
balance=eval(input("Enter the initial deposit: "))
while balance<1000000: #!+ means doesnt equal but dont use it, and be careful with condition
    balance+=.04*balance #balance=balance+(.04*balance) - get altogether by adding balance again
    numberOfYears+=1 #get interest when it's been there for a whole year
print("In", numberOfYears, "years you will have a million dollars")
