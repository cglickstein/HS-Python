#find the minimum, max, and average of a sequence of numbers
count=0 #number of numbers inputted- and assume positive numbers (and 0) put in
total=0 #sum of numbers inputted
#obtain numbers and determine count, min, max
print("Enter -1 to terminate entering numbers: ")
num=eval(input("Enter a non-negative number: "))
min=num #only have one number
max=num #at this moment, still don't have anything else, so it is both

#more correct, make if so that it cant be a neg number
#1 means if not
while num !=-1:
    count+=1
    total+=1 #total is 0 so if you enter 5, total is 5
    #then it starts again
    #count and total are used to find average
    if num<min:
        min=num #blobk of code, max=num is another block so clock within a block
    if num>max:
        max=num
    num= eval(input("Enter a non-negative number: "))
    #keeps starting over so two ifs suffice to find max and min

#display results- not part of loops but keeps altered variables
if count>0: #very important to do
    print("minimum: min", min)
    print("maximum", max)
    print("average", total/count) #total is 0 and you're going to get an error. look back at code
else:
    print("No non-negative numbers enetered")
    #adds onto count but doesn't change min or max
