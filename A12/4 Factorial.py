def getN(n):
    if isinstance(n,int) == True and n>=0:
        return True
    return False



def fadct(n):
    list= []
    var=1
    for i in range(2, n+1): #why is it giving me 120?
        var=var*i
    return var



n=int(input("Please enter a positive integer: "))
if getN(n):
    factorial= fadct(n)
    print(factorial, "is the factorial of", str(n) + ".")

else:
    print("This is not a positive integer.")

