x=0 #DECLARE A GLOBAL VARIABLE

MINIMUM_VOTING_AGE=18 #named constants
MINIMUM_VOTING_AGE=19 #ONLY Python lets you do this- variables that you can change

def main():
    #demonstrate the scope of variables
    #x=2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")

def trivial():
    #x=7 #this is trivial x
    global x #changes everywhere
    x+=7 #it doesn't do this. you can see global variables in any place
    #x=3 global variable used instead
    print(str(x) + ": function trivial")





main()
print(str(x) + ": actual main") #this runs last
