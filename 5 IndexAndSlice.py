            #Python,P=0 (there are 6 positions)
print("Python")
print("Python"[1],"Python"[5],"Python"[2:4])
str1="Hello World"
print(str1[1],str1[6],str1[6:11])
print(str1.find('W'))
print(str1.find('x')) #Wasnt ther so -1
print(str1.find(' '))
print(str1.find('l')) #gives the first l so rfind(reverse)
print(str1.rfind('l'))

print("Python"[-1])
print("Python"[-4],"Python"[-5:-2])
print("Hello World")
print(str1[-2],str1[-5:-1])
print(str1[0:-1]) #missing D
print(str1[0:])
print("again")
print(str1[6:]) #goes all the way until end
print("Python"[:4])
print("Python"[:-3])
print("Python"[:]) #prints it all
