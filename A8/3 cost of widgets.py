#3
widgets=eval(input("Enter amount of widgets ordered"))
if widgets<100:
    print(widgets*.25,"$")
else:
    print(widgets*.20,"$")
