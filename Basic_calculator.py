def add(a, b):
    answer  = a + b
    print('{} + {} = {} \n'.format(a, b, answer))
def sub(a, b):
    answer  = a - b
    print('{} + {} = {} \n'.format(a, b, answer))
def mul(a, b):
    answer  = a * b
    print('{} + {} = {} \n'.format(a, b, answer))
def div(a, b):
    answer  = a / b
    print('{} + {} = {} \n'.format(a, b, answer))

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')

    choice = input('Choose your choice: ')

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Insert fisrt number: '))
        b = int(input('Insert second number: '))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Insert fisrt number: '))
        b = int(input('Insert second number: '))
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Insert fisrt number: '))
        b = int(input('Insert second number: '))
        mul(a, b)
    elif choice == 'd' or choice == 'D':
        print('Division')
        a = int(input('Insert fisrt number: '))
        b = int(input('Insert second number: '))
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('Program Ended.')
        quit()