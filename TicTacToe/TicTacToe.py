import random
# create board
def board(squares):
    board = (
    f"|{squares['1']}||{squares['2']}||{squares['3']}|\n"
    f"|{squares['4']}||{squares['5']}||{squares['6']}|\n"
    f"|{squares['7']}||{squares['8']}||{squares['9']}|\n"
)
    print(board)

squares = {
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

#players - start screen
print('Welcome to TicTacToe!\n'
      'player_1 is \'x\' & player_2 is \'o\''
       )
player1 = input('What is your name player1: ')
def player_input(player1):
    while player1 == player1.isdigit():
        print('No numbers allowed')
        player1 = input('What is your name: ')
    while player1 == "":
        print('you did not enter a name')
        player1 = input('What is your name: ')
    while not player1.find(' ') == -1:
        print('no spaces allowed')
        player1 = input('What is your name: ')
player_input(player1)
player2 = input('What is your name player2: ')
player_input(player2)
print(f'Hello and Welcome {player1.capitalize()} & {player2.capitalize()}')

who_starts = random.ranint(1, 2)
if who_starts == 1:
    print("Based of the random software, player1 will start first\n player1 is \'x\'")
else:
    print("Based of the random software, player2 will start first\n player2 is \'o\'")