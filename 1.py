# :p
def even(n):
    if n is 0:
        exit()
    elif n % 2 is 1:
        print "Odd"
    elif n % 2 is 0:
        print "Even"

def calc(n):
    for i in range(1, 10):
        n += 2
        print(n)

if __name__ == '__main__':
    x = float(input())
    if(x.is_integer() is False):
        print('plz enter type of int')
    elif (int(x) is 0):
        print('do you know zero-divide?')
    else:
        y = int(x)
        calc(y)
        even(y)
