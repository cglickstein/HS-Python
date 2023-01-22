wholeNumber=int(input("Enter a whole number greater than 1: "))

divisor=1
while divisor<=wholeNumber:
    if wholeNumber%divisor==0:
        print(divisor)
    divisor+=1
