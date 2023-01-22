def getmax(numb):
        list=[]
        while numb != "!":

            list.append(numb)
            numb= input("Please enter another number: ")

        list.sort(reverse=True)
        maxNum= list[0]
        return maxNum


#loop then append
print("To finish entering numbers at any time, please enter \"!\"...")
numb=input("Please enter the first number: ")
max= getmax(numb)

print(max, "is the highest number.")

