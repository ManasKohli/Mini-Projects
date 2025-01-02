# Hangman Game
print('Welcome to HangMan!')
print('You will have 10 strikes to guess the secret word.')

# Secret word and game setup
word = "january"
letters = ['-' for _ in word]  # Initialize hidden word as dashes
strikes = 0  # Initialize strike counter

# Main game loop
while True:
    # Display strikes and remaining attempts
    if strikes == 1:
        print(f'You have used {strikes} strike, {10 - strikes} remain.')
    else:
        print(f'You have used {strikes} strikes, {10 - strikes} remain.')

    # Display the current state of the guessed letters
    print(' '.join(letters))
    
    # Prompt user for their guess
    guess = input('What letter do you pick: ').lower()

    # End the game if the user has used all strikes
    if strikes == 9:
        print('All 10 strikes used. Game over! The word was January. ')
        break

    # Update the letters if the guess is correct
    if guess == 'a':
        letters[1] = 'a'
        letters[4] = 'a'
    elif guess == 'j':
        letters[0] = 'j'
    elif guess == 'n':
        letters[2] = 'n'
    elif guess == 'u':
        letters[3] = 'u'
    elif guess == 'r':
        letters[5] = 'r'
    elif guess == 'y':
        letters[6] = 'y'
        # Handle invalid guesses
        if guess not in 'january':
            strikes += 1  # Increment strike counter for wrong guesses
            print('That letter is not in the secret word. Try again.')
        if not guess.isalpha():
            print('Invalid input. Only letters are allowed!')

    # Check if the player has guessed the word
    if letters == list(word):
        print('Congratulations! You guessed the word!')
        print(' '.join(letters))
        break
