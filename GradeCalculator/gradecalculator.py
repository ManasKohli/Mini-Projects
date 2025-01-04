def average():
    def is_numeric(value):
        """Check if a string is a valid number (integer or float)."""
        try:
            float(value)
            return True
        except ValueError:
            return False

    grades = []  # List to store valid grades

    while True:
        try:       
            user_grade = input('Enter grade (or type "done" to finish): ')
        
            if user_grade.lower() == 'done':
                break

            # Check if the input is numeric
            if not is_numeric(user_grade):
                print('Only numbers allowed.')
                continue

            # Convert to float and validate the grade range
            user_grade = float(user_grade)
            if 0 <= user_grade <= 100:
                grades.append(user_grade)
            else:
                print('You did not enter a valid grade. Please enter a number between 0 and 100.')

        except ValueError:
            print('Value Error, try again.')

# Calculate the average if there are valid grades
    final_average = sum(grades) / len(grades)
    print(f'\nYour average was {round(final_average, 2)}%')

def final():
    # Initialize lists to store grades and weights
    grades = []
    values = []

    while True:
       
        # when final grades are calculated
        if sum(values) == 1:
            break
        
        grade = input('Put your grade: ').strip()
        
        # Validate and convert the grade input
        try:
            grade = float(grade)
            if not 0 <= grade <= 100:
                print('Invalid grade. Must be between 0 and 100. Try again.')
                continue
            else:
                grades.append(grade)
        except ValueError:
            print('Invalid grade. Please enter a number.')
            continue
        
        # Get and validate the weight
        value = input('How much is it worth? (e.g., if 20%, type 0.2): ').strip()
        
        try:
            value = float(value)
            if not 0 < value <= 1:
                print('Invalid value. Must be between 0 and 1. Try again.')
                continue
            else:
                values.append(value)
        except ValueError:
            print('Invalid value. Please enter a number.')
            continue

    # Calculate the weighted grade
    if grades and values:
        final_grade = sum(a * b for a,b in zip(grades, values))
        print(f'\nYour final weighted grade is: {round(final_grade, 2)}%')
    else:
        print('\nNo grades or values were entered.')


print('Do you want to calculate your final grade with'
      'each grade being worth a certain %?,'
      )
print('Or do you just want the general average, meaning all grades are the same amount?')
print('If you want final grade type \'final\' ')
print('If you want general average type \'general\'')

user = input('What would you like to proceed with: ')
if user.lower() == 'general':
    average()
else:
    final()

