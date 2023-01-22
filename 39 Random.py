import random

elements= ['earth', 'air', 'fire', 'water']
print(random.choice(elements))
print(random.sample(elements,2))
random.shuffle(elements) #random is a mutable list so you can change it- chamnge order
print(elements) #now its already shuffled

myString='happy'
mtList=[]
for letter in myString:
    mtList.append(letter)

random.shuffle(mtList)
print(mtList)
print("".join(mtList))

print(random.randint(1,5))
