myList=[4,5,3]
myList.sort(reverse=True) #puts it in number order
print(myList)

myListA=["cat","dog","apple"] #from lowest value to highest value
myListA.sort(reverse=True) #sort puts in alphabetical order and reverse makes it start from z to a
print(myListA)

highScore=[6,3,5]
score=int(input("What is your score?: "))
highScore.append(score)
print(highScore)
#always want to just have 3 high scores
highScore.sort() #starts with lowest numbers but you want the highest scores
highScore.sort(reverse=True)
print(highScore)
highScore=highScore[0:3]
