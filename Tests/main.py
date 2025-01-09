balance = 0

def show_balance():
    print(f'Your balance is {balance}$')
    

def bank_deposit():
    
    deposit = float(input('How much do you want to deposit: '))
    return deposit

            
def withdraw():
    
    withdrawal = float(input('how much do you want to withdraw'))
    return withdrawal





print('WeBull Bank')
print( '1. Show balance\n'
       '2. Deposit \n'
       '3. Withdraw \n'
       '4. Exit \n'

)

while True:
    
    try:
        choice = input('choice (1-4): ')

        if int(choice) == 1:
            show_balance()

        elif not 1 <= int(choice) <= 4:
            print('No option chosen')

        elif int(choice) == 2:
            
            balance = balance + bank_deposit()
            print(f'New balance is ${balance:.2f}')
        
        elif int(choice) == 3:
            
            balance -= withdraw()
            print(f'New balance is ${balance:.2f}')


    
    
    except ValueError:
        print('Try again value error')



