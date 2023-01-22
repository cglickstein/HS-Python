wholeNumber=int(input("Enter a whole number greater than 1: "))

divisor=2
counter=2
prime=True
while divisor<=wholeNumber:
    if wholeNumber%divisor==0:
        #found factor
        factor=divisor

        while factor>counter:
            if factor%counter==0:
                prime=False
            counter+=1
        if prime==True:
            print(factor)


    divisor+=1
    counter=2 #reset counter
    prime=True #reset prime
