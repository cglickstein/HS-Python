def semesterGrade(midterm, final):
    g=((midterm/3)*2+final/3)
    g=ceil(g)


    if g >=100:
        g="A"
    elif g>=80 and g<=89:
        g= "B"

    elif g>=70 and g<=79:
        g= "C"

    elif g>=60 and g<=69:
        g= "D"

    elif g<60:
        g= "F"
    return g


def ceil(grade):
    a= round(grade, 0)
    a=int(a)
    return a



midterm=eval(input("Enter numeric midterm grade: "))
final=eval(input("Enter numeric final grade: "))
grade=semesterGrade(midterm, final)
print("Your grade for this semester is a(n)", grade + '.')
