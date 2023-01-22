print("012345678901234567890")
print("{0:10d}" .format (12345678) )#digit- no decimal
print("{0:10,d}".format(12345678)) #Thousands place seperators
print("{0:10.2f}".format(1234.5618)) #float-deci, .2-#deci
print("{0:10,.2f}".format(1234.5678))
print("{0:10,.2%}".format(1234.5678)) #makes percentage for you

print("The area of {0:s} is {1:,d} square miles." .format ("Texas",268820)) #matches formats. s is string and d is digit

str1= "The population of {0:s} is {1:.2%} of the US population" #places after decimal in Perecntage= .2
print(str1.format ("Texas",264488000/309000000))

print(" state1 {1:s} and state2 {0:s}. {0:s} is bigger".format("Texas","Maryland"))
