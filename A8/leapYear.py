#leapYear
year=eval(input("Enter a year: "))
year1=str(year)
if year//4 and year1.endswith("00"):
    print("Year is a leap year")
else:
    print("Year is not a leap year!")
