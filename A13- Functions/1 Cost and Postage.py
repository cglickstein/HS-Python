def cost(oz):
    if oz>1:
        oz-=1
        oz= .05+ (oz*.10)
    if oz==1:
        oz= .05
    return oz



oz=eval(input("Please enter the letter's weight in ounces: ")) #whole number? 2. not two deci places
weight= cost(oz)
weight=("${0:,.2}").format(weight)
print("Cost:", weight)
