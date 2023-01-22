#var called flag, and flag is bulyian (yes or no, up or down, true or false)
#find the first inetger divisible by 11
list1=["one",23,17.5,"two",33,32.1,242,"three"]
i=0
'''while i<8: #or i<len(list1)
    print(list1[i])
    i+=1 #you can print everything up to 8 instead of'''



foundFlag=False #forces it to go into while (first time around)
while i<len(list1) and foundFlag==False:              #foundFlag==False: goes out of range
    x=list1[i]
    i+=1
    if not isinstance(x, int): #boolean (True/False)- sees if first thing in list is integer
        #only number without decumal. is this number instance of int?
        #not true= false

        continue #goes to next thing produced by loop #skip to next item in list (check condition)
        #go back and check loop again

    if x%11==0:
        foundFlag= True

        print(x, "is the first int that is divisible by 11")

#once it's true, it now comes out of if and the while
print("the end")
