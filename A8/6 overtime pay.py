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
    print("{0:10.2f}".format (hours*wage)+"$")
