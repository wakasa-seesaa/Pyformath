# need take time to think...
# Remember Divide-and-Conquer method as for top-down approach.
def even(n):
    if n is 0:
        exit()
    elif n % 2 is 1:
        return 1
    elif n % 2 is 0:
        return 0

def calc(n):
    val = even(n)
    

if __name__ == '__main__':
    x = float(input())
    if(x.is_integer() is False):
        print('is not integer')
    elif (int(x) is 0):
        print('do you know zero-divide?')
    else:
        y = int(x)
        if (y % 2 is 0):
            for i in range( 1, 10 ):
                y += 2
                print(y)
            print('even')
        if (y % 2 is not 0):
            for i in range( 1, 10 ):
                y += 2
                print(y)
            print('is not even')
