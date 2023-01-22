justices= ['Scalia R', 'Kenedy R', 'Thomas R', 'Ginsburg D', 'Breyer D', 'Roberts R', 'Alito R', 'Sotomayor D', 'Kagan D']
R = []
D = []

for i in justices:
    if i[-1]== 'R':
        R.append(i)
    else:
        D.append(i)

print(R, "is the list of Republicans")
print(D, "is the list of Democrats")
