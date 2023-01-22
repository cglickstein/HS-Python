#militaryTime
mtime=input("Enter military time from 0000 to 2359: ")
hours=mtime[:2]
hours= int(hours) #?
mins=mtime[2:]
#hours1=str(hours)

if hours== 00: #hours1.startswith("00"):
    print(12,":",mins, "AM", sep='')

elif hours >12 and hours<24:
    print(hours,":",mins, "PM", sep='')

elif hours <12:
    print(hours,":",mins, "AM", sep='')

