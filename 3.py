def print_menu():
    print('1. Kilometers to Miles')    
    print('2. Miles to Kilometers')
    print('3  Celsius to Fahrenheit') 
    print('4  Fahrenheit to Celsius')
def km_miles():
    km = float(input('Enter distance in kilometers: '))
    miles = km / 1.609
    print('Distance in miles: {0}'.format(miles))

def miles_km():
    miles = float(input('Enter distance in miles: '))
    km = miles * 1.609
    print('Distance in kilometers: {0}'.format(km))

def celsius_fahrenheit():
    celsius = float(input('Enter temperature in celsius'))
    fahrenheit = ( 9 / 5 * celsius) + 32
    print('Temperature in celsius: {0}'.format(fahrenheit))

def fahrenheit_celsius():
    fahrenheit = float(input('Enter temperature in fahrenheit'))
    celsius = (5 / 9) * (fahrenheit - 32)
    print('Temperature in fahrenheit: {0}'.format(celsius))

if __name__ == '__main__':
    print_menu()
    choice = input('Which conversion would you like to do?: ')
    if choice is '1':
        km_miles()
    if choice is '2':
        miles_km()
    if choice is '3':
        celsius_fahrenheit()
    if choice is '4':
        fahrenheit_celsius()
