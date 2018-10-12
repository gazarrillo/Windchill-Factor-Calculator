def userInput():
    """This function asks for a temperature and speed and returns those interger values"""
    temperature = int(input('Enter temperature in farenheit: '))
    speed = int(input('Enter the wind speed in mph: '))
    return temperature, speed

def windchillFactor():
    """This function calculates the windchill factor using the userInput() function"""
    temperature, speed = userInput()
    windchill = 35.74 + 0.6215 * temperature - 35.75 * speed**0.16 + 0.4275 * temperature * speed**0.16
    return windchill

def result():
    """This function prints the results of the windchillFactor() function and rounds them to one decimal place"""
    print('The windchill is:', round(windchillFactor(), 1), '\n')

result()

#Loop to calculate more than one windchill factor

cont = input('Would you like to calculate another windchill? Enter "y" or "n": ')

while cont == 'y':
    result()
    cont = input('Would you like to calculate another windchill? Enter "y" or "n": ')
