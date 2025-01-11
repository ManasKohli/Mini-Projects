spaces = {
    '0' : 0,
    '1' : 1,
    '2': 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    '/' : '/',
    'x' : 'x',
    '-' : '-',
    '+' : '+',
    '=' : '='
}

count = 0

def cal_row(a, b, c, d):
    print( f'|{spaces[a]}||{spaces[b]}||{spaces[c]}||{spaces[d]}| \n')


def display():
    cal_row('7', '8', '9' , '/')
    cal_row('4', '5', '6', '-')
    cal_row('1','2','3','+')
    print( f'   |{spaces['0']}|   |{spaces['=']}|')
    

while True:
    display()
    while True:
        count += 1
        choice = float(input(f'Input number{count} to be calculated or type "=" to calculate: '))
        operator = input ('operator (+,-,x,/): ')

        if choice == '=':
            break


  




