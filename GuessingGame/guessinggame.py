import random

# Introduction to the game
print('Welcome to the Guessing Game!')
print('Try to guess a number between [1 and 100]')

# Generate a random number between 1 and 100
random_num = random.randint(1, 100)

# Main game loop
while True:
    try:
        # Prompt the user for their guess
        guess = int(input('Guess a number: '))

        # Check if the guess is higher than the target number
        if guess > random_num:
            print('Too high! Try again.')
        # Check if the guess is lower than the target number
        elif guess < random_num:
            print('Too low! Try again.')
        # If the guess is correct, congratulate the user and exit the loop
        else:
            print(f'Congratulations! You guessed the correct number {random_num}!')
            break
    except ValueError:
        # Handle non-numeric input
        print('Invalid input! Please enter a valid number.')


        


