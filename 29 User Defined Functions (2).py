def fahrenheitToCelsius(t):
#t+=2 changing t won't change fahrenheit. 2 people with the same name will stay seperate even though they go back into what's in the parenthesis as the same thing
    convertedTemperature= (5/9) * (t-32)
    return convertedTemperature #gets assigned into
    print(convertedTemperature) #it would not do this because once you return something, the block of code is done


#main
fahrenheitTemp= eval(input("Enter a temperature in degrees Fahrenheit: "))
convertedTemperature= "abcdefg" #prints this out because the one above is totally different
celsiusTemp= fahrenheitToCelsius (fahrenheitTemp)
celsiusTemp= round(celsiusTemp, 2)
print("Celsius equivalent is", celsiusTemp, "degrees.")
