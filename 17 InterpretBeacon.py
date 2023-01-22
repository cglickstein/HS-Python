#Weather forecast light on top of Boston's
#John Hancock building
#steady blue, clear blue
#steady red, rain ahead
#flashing red, snow instead

color=input("Enter a color(BLUE or RED): ")
mode=input("Enter a mode(STEADY or FLASHING): ")
color=color.upper() #important 2 lines of code because now variable holds this permanently
mode=mode.upper()
#analyze responses and display weather
result=""
if color=="BLUE":
    if mode=="STEADY":
        result="Clear View"
    else: #mode is flashing
        result="Rain Ahead"

else:
    if mode=="STEADY":
        RESULT="Rain Ahead"
    else: #mode is flashing
        result="Snow Ahead"


print("The weather forecast is", result)
