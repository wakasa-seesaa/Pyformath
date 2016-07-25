from fractions import Fraction
def add(a, b):
    print('Result of Addition: {0}'.format(a, b, a + b))

def sub(a, b):
    print('Result of Addition: {0}'.format(a, b, a - b))

def div(a, b):
    print('Result of Divide: {0}'.format(a, b, a * b))

def mul(a, b):
    print('Result of Multiply: {0}'.format(a, b, a / b))

if __name__ == '__main__':
    try:
        a = Fraction(input('Enter first fraction: '))
        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perfome - Add, Substract, Divide, Multiply: ')
        if op == 'Add':
            add(a, b)
        if op == 'Substract':
            sub(a, b)
        if op == 'Divide':
            div(a, b)
        if op == 'Multiply':
            mul(a, b)
    except:
        print("caught something")
