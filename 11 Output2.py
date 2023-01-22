print("012345678901234567890")
print("Rank".ljust(5),"Player".ljust(20),"HR".rjust(3),sep="")#sinceRank is not 5 spaces long it will make a space
print("1".center(5), "Barry Bonds".ljust(20),"762".rjust(3),sep="")
print("2".center(5), "Hank Aaron".ljust(20),"755".rjust(3),sep="")
#print("123456".center(5), "Hank Aaron".ljust(20),"755".rjust(3),sep="")#will push off allignments because it takes up more space
print("0123456789012345678901234567890")
#^=center allign,< is left allign,> is right allign
print("{0:^5n}{1:<20s}{2:>3n}".format(1.,"Barry Bonds",762))#s=string, n=number so dont put the numbers in quotes,
# then it will think it is a string
print("{0:^5n}{1:<20s}{2:>3n}".format(2.,"Hank Aaron",755))#lined up
print("{0:10d}".format(12345678))#d=digits-integer, it right alligns digits
print("{0:10,d}".format(12345678))
print("{0:10.2f}".format(12345.678))#f=float- 2 tells it how many decimal places. I you dont show it will do six.
#If you also do a "," then it will make comma place separator
