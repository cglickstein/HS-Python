year=eval(input("Please enter a year to see if it's a leap year: "))
#take 1582 into account

if year/4== year//4:
    if year/100 == year/100 and year/400 == year//400:
        print(year, "is a leap year.")
    else: print(year, "is not a leap year.")

else:
    print (year, "is not a leap year.")
