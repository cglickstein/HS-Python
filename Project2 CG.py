import random
list= []


low=eval(input("Welcome User! Please choose a low number in the range: "))
high=eval(input("Please choose a high number in the range: "))

n=random.randint(low,high)
print( ) #GET RID OF THIS AT THE END and turn to false
print("Think of the chosen number between", low, "and", high, ".This includes", high,"too...")

#Acquiring a valid integer guess for the first time before entering while loop
integer=False
while integer== False :
    try:
        guess=int(input("Please guess that number here: "))/1.0
        list.append(guess)
        break
    except ValueError:
        print("Invalid input. Please enter an integer...")


#Pre-loop variables
count=0
flag = False
var = True
integer = False

#ACTUAL PROGRAM
while flag== False:
    #isisntance(guess,int) STATUS: THIS DIDNT WORK, HAD TO USE TRY, EXCEPT BLOCK!

    if guess>high or guess<low:
        print("This is not a valid guess as it is not between the correct range. Try again.")

        while integer == False:
            try:
                guess = int(input("Please guess a new number here: "))/1.0
                list.append(guess)
                break
            except ValueError:
                print("Invalid input. Please enter an integer...")


    elif guess==n:
        print( )
        print ("Congratulations, you guessed the right number! It was " + str(n) + ".")
        count+=1
        print( )
        print("...I just can't believe it took you", count, "time(s) to guess right!")
        print( )
        #print(list)
        again=input("Enter Y to start over or N to terminate: ").upper()

        if again== "Y":
            low=eval(input("Welcome User! Please choose a low number in the range: "))
            high=eval(input("Please choose a high number in the range: "))
            n=random.randint(low,high)
            print( )
            while integer == False:
                try:
                    guess = int(input("Please guess a new number here: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer...")

        else:
            flag== True
            break


    elif guess<n:
        print( )
        print(int(guess), "is too low. Try guessing a higher number.")
        count+=1
        while integer == False:
            try:
                guess = int(input("Please guess a new number here: "))/1.0
                for i in list:
                    if guess != i:
                        continue
                    else:
                        print("You already guessed this. Guess again!")
                        break

                list.append(guess)
                break

            except ValueError:
                print("Invalid input. Please enter an integer...")


    elif guess>n:
        print( )
        print(int(guess), "is too high. Try guessing a lower number.")
        count+=1
        while integer == False:
            try:
                guess = int(input("Please guess a new number here: "))/1.0
                for i in list:
                    if guess != i:
                        continue
                    else:
                        print("You already guessed this. Guess again!")
                        break

                list.append(guess)
                break

            except ValueError:
                print("Invalid input. Please enter an integer...")



print( )
print("Thank you for playing!")





