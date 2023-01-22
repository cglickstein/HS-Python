#Calculate the average of grades
grades=[]
num=float(input("Enter the first grade:"))
grades.append(num) #anything in parameters added to list named "grades"
print(grades) #Num added just to put things in list (can keep variable)

num=float(input("Enter the second grade:"))
grades.append(num)

num=float(input("Enter the third grade:"))
grades.append(num)

num=float(input("Enter the fourth grade:"))
grades.append(num)

num=float(input("Enter the fifth grade:"))
grades.append(num)

minimumGrade=min(grades)
print("minimum grades", minimumGrade)
maximumGrade=max(grades)
print("maximum grades", maximumGrade)
grades.remove(minimumGrade)
print(grades) #excludes lowest grade with no empty space
#if two lowests that are same, only removes the first it encounters
average=sum(grades)/len(grades)
print("Average grade: {0:.2f}".format(average)) #0ith thing is average
#"string{}".format(average)
#[12,43}.append(18) - same thing
#my average{0:.2f}".format(343.343)
#always object.(arguments)

names=["Jane", "John","Jenny", "Abc"]
names.append("Julie")
print(names)
minimum=min(names)
print(minimum) #smaller goes by alphabetical order
print(len(names))
names.remove("Abc")
print(names)
