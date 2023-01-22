score1=eval(input("Enter the 1st score: "))
score2=eval(input("Enter the 2nd score: "))
score3=eval(input("Enter the 3rd score: "))
mn = score1
if score2<mn:
    mn = score2
if score3<mn:
    mn=score3
lON= [score1, score2, score3]
lON.remove(mn) #Dont do variable equals variable.remove
a = (lON[0] + lON[1])/2
print(a)

    '''#7 Compute an average
score1=eval(input("Enter the 1st score: "))
score2=eval(input("Enter the 2nd score: "))
score3=eval(input("Enter the 3rd score: "))
m = score1
if score2<m:
    m = score2
if score3<m:
    m=score3
lON= [score1, score2, score3]
lON.remove(m) #Dont do variable equals variable.remove
a = (lON[0] + lON[1])/2
print(a)'''
