grade=int(input("Enter numeric grade: "))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=65:
    print("D")

else:
    print("F")

#dont do a bunch of ifs-code taking more power and fulfills all
#with elif as soon as it goes into one condition it stops. would be a c and b and d and f otherwise
#if requirement for D is first then it would say that you got a D... be careful

grade=int(input("Enter numeric grade: "))
if grade>=90:
    letterGrade="A"
elif grade>=80:
   letterGrade="B"
elif grade>=70:
   letterGrade= "C"
elif grade>=65:
    letterGrade="D"

else:
    print("Your final grade is",letterGrade)
