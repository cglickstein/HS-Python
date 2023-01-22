'''COR= eval(input("Enter coefficient of restitution (between 0 and 1): "))
height= eval(input("Enter the initial height in meters: "))
#newHeight= height*COR
firstBounce= 1
distance= height
while height>.10:
    height= height*COR
    firstBounce= firstBounce + 1
    distance= height*2+distance
print("The ball bounced", firstBounce, "times.")
print("The distance is", distance, "meters")
    #print("The total distance traveled by the ball is", distance, "meters")'''


COR= eval(input("Enter coefficient of restitution (between 0 and 1): "))
height= eval(input("Enter the initial height in meters: "))
#newHeight= height*COR
firstBounce= 0
distance= height
while height>.10:
    height= height*COR
    if firstBounce == 0:
        distance = height+ distance #
    else:
        distance= height*2+distance
    firstBounce= firstBounce + 1

print("The ball bounced", firstBounce, "times.")
print("The distance is", distance, "meters")
    #print("The total distance traveled by the ball is", distance, "meters")
