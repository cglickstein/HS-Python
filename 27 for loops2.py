#using a tuple
months =("Jan", "Feb", "Mar", "Apr")
for month in months: #months is made up word looking at actual tuple months
    if 'r' in month.lower():
        print(month)

months =["Jan", "Feb", "Mar", "Apr"]
for month in months: #months is made up word looking at actual tuple months
    if 'r' in month.lower():
        print("yes")

months= ["January", "February", "March", "April"]
for i in range(len(months)): #i starts off as 0: same as for i in range(4)
    months[i] =months[i][:3] #takes 0th item so jan
print(months)

#this would't work with a list 9cant change or take slices)
