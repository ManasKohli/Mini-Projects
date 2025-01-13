cal = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', 'x'],
    ['1', '2', '3', '-'],
    [' ', ' ', '0', '+']
]

def board(cal):
    for i in cal:
       print(' '.join(map(str, i)))


def results(num1, num2, operator):
    operations = {
        '/': lambda x, y: round(x / y, 2) if y != 0 else "Undefined (division by zero)",
        '+': lambda x, y: round(x + y, 2),
        '-': lambda x, y: round(x - y, 2),
        'x': lambda x, y: round(x * y, 2),
        '^': lambda x, y: round(x ** y, 2)
    }
    result = operations[operator](num1, num2)
    print(f'Result is: {result}')


def check(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


while True:
    board(cal)

    num1 = input('First number or type "quit": ')

    if num1.lower() == 'quit':
        break

    if not check(num1):
        print('Only numbers are allowed.')
        continue

    num1 = float(num1)

    try:
        operator = input('Operator (/, +, -, x, ^): ')
        if operator not in ('-', '+', '^', '/', 'x'):
            print('Invalid operator.')
            operator = input('Operator (/, +, -, x, ^): ')
            
    except ValueError:
        print('Value error')
        continue

    num2 = input('Second number or type "quit": ')

    if num2.lower() == 'quit':
        break

    if not check(num2):
        print('Only numbers are allowed.')
        num2 = input('Second number or type "quit": ')

    num2 = float(num2)

    # Call the `results` function with the operator
    results(num1, num2, operator)

  
    
 