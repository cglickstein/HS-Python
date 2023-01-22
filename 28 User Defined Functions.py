def getFirstName(full): #this is a totally different full name because it's in a different block of code
    firstSpace=full.index(" ")
    givenName=fullName[:firstSpace]
    return givenName
#change full? dont change full name. full name being sent to full, and it's same thing- matches first item in parenthesis



#main- where the code starts. def is ignored and has to be called
fullName= input("Enter your full name: ")
firstName=getFirstName(fullName) #send function to find first name, full name... def is being called here
#getfirstname function is argument. We're sending it the formal parameter which starts as actual parameter
print(firstName)

#main- where the code starts. def is ignored and has to be called
student1= input("Enter your full name: ")
firstName=getFirstName(student1) #send function to find first name, full name... def is being called here
#getfirstname function is argument. We're sending it the formal parameter which starts as actual parameter
print(firstName)

student2= input("Enter your full name: ")
firstName=getFirstName(student2) #assigning value of student2 to full
print(firstName)
