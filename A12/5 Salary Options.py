def option1(pay):
    return (100*days)

def option2(pay):
    money=1
    for i in range(10):
        money*=2
    return money



def compare(option1, option2):
    if option1>option2:
        return "Option1"
    else:
        return "Option2"

days=10
one= option1(days)
two= option2(days)
greater= compare(one, two)
print("Option 1 pays${0:,.2f}".format(one))
print("Option 2 pays:${0:,.2f}".format(two))
print(greater,"is better." )
