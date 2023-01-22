#1 Tip
check=eval(input("Enter bill on check: "))
tip=check*.15
minimumTip=2
if tip<minimumTip: #dont forget the :
    print("Tip should be more than 2$")
else:
    print(tip,"$")
