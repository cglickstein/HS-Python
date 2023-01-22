dig1= int(input ("Enter the first integer: "))
dig2= int(input ("Enter the second integer: "))
divisor= 1
counter=0

while dig1>counter and dig2>counter:
        if dig1%divisor==0 and dig2%divisor==0:
                possibleDivisor=divisor
        divisor= divisor + 1
        counter+=1

print(possibleDivisor, "is the greatest common divisor.")
