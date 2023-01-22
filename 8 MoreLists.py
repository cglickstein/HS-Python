#Type of data that can hold many dif types of data
#imutable-variables can't be changed(can be redirected) while lists can be changed and mutated(add,subtract,delete while moves everything to the left(resizes)

myList=[0]


nums=[5,10,4,5]
words=["spam","ni"]
print(len(words))
print(max(nums))
print(max(words))
#lowest letter is A rather than a
#Upper case letters are lower than any uppercase
words=["ZOO","apple"]
print(max(words))
#can only sum lists that are numbers
print(sum(nums))
#cant print sum of words
print(words.count("ZOO"))
print(nums.index(4)) #What index is the four in?
words[0].count("O") #YOU HAVE TO TAKE EACH WORD SEPERATELY BECAUSE CAN'T FIGURE OUT IN ENTIRE STRING
print(words.index("ZOO")) #gives what's in the first index
words.reverse()#action
print(words) #now in oppsoite order
#Now the index of zoo is 1(first item in the list)
words.clear()
print(words) #clear makes it empty
nums.extend([7]) #You need number in square brackets with regular parethesis on the outside
print(nums)
nums.extend([1,2]) #with extend you can attach a whole new list and not just one item/number
del nums[-1] #DEL is delete
print(nums) #takes last number off
nums.remove(5)
print(nums)
words=["ZOO","apple","O"]
words.insert(1,"wink") #already reversed
newList=nums+words #can concatenate lists
print(newList)
print(words*3) #list repeated three times within own list

#REFER TO LIST SLICES FOR MORE ON TABS AND JOIN
print("a,b,cd".split(',')) #you can now rejoin and makes a list
