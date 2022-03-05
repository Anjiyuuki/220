def first_while():
    for i in range(5):
        print(i, end='')
    print('\n{0:*<70}'.format(''))
    i = 0
    while i <5:
        print(i, end='')
        i = i + 1

if __name__ == '__main__':
    first_while()
