import random

# Create board
def board(squares):
    board = (
        f"|{squares['1']}||{squares['2']}||{squares['3']}|\n"
        f"|{squares['4']}||{squares['5']}||{squares['6']}|\n"
        f"|{squares['7']}||{squares['8']}||{squares['9']}|\n"
    )
    print(board)

# Initialize squares
squares = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

# Players setup
print('Welcome to TicTacToe!\n'
      'player_1 is \'X\' & player_2 is \'O\''
      )
player1 = input('What is your name, player1: ')
def input_name(player1):
    while player1 == '' or player1.isalpha() == False or not player1.find(' ') == -1:
        if player1 == '':
            player1 = input('what is your name, player1: ')
        elif player1.isalpha() == False:
            player1 = input('No numbers allowed, what is your name: ')
        elif not player1.find(' ') ==-1:
            player1 = input('no spaced allowed, what is your name: ')
input_name(player1)
player2 = input('What is your name, player2: ')
input_name(player2)
print(f'Hello and Welcome {player1.capitalize()} & {player2.capitalize()}')

# Randomize who starts
who_starts = random.randint(1, 2)
if who_starts == 1:
    print("Based on the random software, player1 will start first (\'X\').")
else:
    print("Based on the random software, player2 will start first (\'O\').")

# Playing instructions
print('Let\'s now start the game! Type \'q\' to stop the game.')

turn = 0
a = 'X'
b = 'O'
endmessage1 = 'GAME OVER: PLAYER 1 WINS'
endmessage2 = 'GAME OVER: PLAYER 2 WINS'

# Determine whose turn it is
def check_turn(turn):
    if who_starts == 2:
        return 'X' if turn % 2 == 0 else 'O'
    elif who_starts == 1:
        return 'O' if turn % 2 == 0 else 'X'

# Check for a winner
def winner(squares, player_mark, endmessage):
    if squares['1'] == player_mark and squares['2'] == player_mark and squares['3'] == player_mark:  # Top row
        print(endmessage)
        return True
    elif squares['4'] == player_mark and squares['5'] == player_mark and squares['6'] == player_mark:  # Middle row
        print(endmessage)
        return True
    elif squares['7'] == player_mark and squares['8'] == player_mark and squares['9'] == player_mark:  # Bottom row
        print(endmessage)
        return True
    elif squares['1'] == player_mark and squares['4'] == player_mark and squares['7'] == player_mark:  # Left column
        print(endmessage)
        return True
    elif squares['2'] == player_mark and squares['5'] == player_mark and squares['8'] == player_mark:  # Middle column
        print(endmessage)
        return True
    elif squares['3'] == player_mark and squares['6'] == player_mark and squares['9'] == player_mark:  # Right column
        print(endmessage)
        return True
    elif squares['1'] == player_mark and squares['5'] == player_mark and squares['9'] == player_mark:  # Diagonal 1
        print(endmessage)
        return True
    elif squares['3'] == player_mark and squares['5'] == player_mark and squares['7'] == player_mark:  # Diagonal 2
        print(endmessage)
        return True
    return False

# Game loop
while True:
    board(squares)
    choice = input('Which square: ')

    # Check for quit command
    if choice.lower() == 'q':
        print("Game Over. Thanks for playing!")
        break

    # Validate input
    while not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or squares[choice] in ['X', 'O']:
        if not choice.isdigit():
            choice = input('Only numbers are allowed. Which square: ')
        elif int(choice) < 1 or int(choice) > 9:
            choice = input('Only numbers between 1 and 9 are allowed. Which square: ')
        elif squares[choice] in ['X', 'O']:
            choice = input('You already used that square. Choose another square: ')

    # Update the board
    turn = turn + 1
    squares[choice] = check_turn(turn)
   

    # Check for a winner
    if winner(squares, 'X', endmessage1) or winner(squares, 'O', endmessage2): 
        board(squares)
        break
       

    # Check for a draw
    if all(isinstance(value, str) for value in squares.values()):
        print("It's a draw!")
        board(squares)
        break


