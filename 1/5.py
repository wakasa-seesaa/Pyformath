def multi_table(a):
    for i in range(1, 11):
        print('{0} x {1} = {2}'.format(a,i,a*i))

if __name__ == '__main__':
    while True:
        a = input('Enter a number.')
        multi_table(float(a))

        answer = input('if you exit this program, enter exit.')
        if answer == "exit":
            break
