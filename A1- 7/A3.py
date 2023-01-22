
# 1
n = eval(input("Enter number of second between lightning and thunder"))
storm = n / 5
print(round(storm, 2), "miles")

# 2
a = eval(input("Enter your age"))
r = eval(input('Enter your resting heart rate(your pulse when you first awaken'))
THR = 7 * (220 - a) + .3 * r
print(THR, "/min")

# 3-Triatholon
c = eval(input("Enter number of hours spent cycling")) * 200
r = eval(input("Enter number of hours spent running")) * 475
s = eval(input("Enter number of hours spent swimming")) * 275
cal = c + r + s
print((cal / 3500), "pounds")

# 4
kWh = 11.76 * 100  # Was 11.76 supposed to be $, not cents?               #cost of electricity instead of kWh?
w = eval(input("Enter wattage of device"))
h = eval(input("Enter hours used (on device)"))
e = (w * h) / (1000 * kWh)  # is there a way i need to change 11.76 into all cents if not? if not, maybe move 11.76 down here
print(e, "dollars")


#5
a=(input("Enter name of baseball team"))
b=eval(input("Enter number of games won"))
c=eval(input("Enter number of games lost"))
p=b/(b+c)
p*=100
p=round(p,1)
print(a,p, "%")

#6
p=eval(input("Enter percent number"))
d=p/100
print(d)

#7
e=eval(input("Enter earnings per share for the year"))
s=eval(input("Enter price per share of stock"))
r=s/e
print(r)       #WHATS WRONG WITH THIS?

#8
d=eval(input("Enter distance skidded in feet"))
s=(24*d)**.5
print(s,"Miles/hour")

#9
k=eval(input("Enter speed in kilometers per hour"))
m=k*.6214
print((round (m,2),"MPH"))

#10
a=eval(input("Enter the amount of thie bill"))
p=eval(input("Enter the perecentage tip"))
p/=100
tip=(p*a)
print("$",round(tip,2))


#11
pn=(input("Enter a positive number containing a decimal")) #not a string so no need for eval
decimal=(pn.find("."))
print(decimal, "digits to the left of decimal")
length= len(pn)
print(length-(decimal+1), "digits to the right of decimal")


#12
a=input("Enter a sentence")
b=input("Enter a word in the sentence (to replace)")
c=input("Enter another word(replacement word)")
print(a .replace(b,c))


#13
a=eval(input("Enter a whole number of months"))
y=a//12
m=a%12
print(y, "years",m,"months")


