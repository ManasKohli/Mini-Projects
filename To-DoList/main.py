

# Initialize the list and counter
todo = []
count = 0


print('Welcome to the to-do list')
print("When all tasks are added, type 'done'")
print('type delete to remove a task')
print()


# Function to display the to-do list
def display_list():
    
    print('To-Do List:')
    
    for x in todo:
            print(x)
            print(' ')
    print()  # Add a blank line for readability




while True:
    try:
        # Clear and display the current list
        display_list()
        
        # Prompt user to add a task
        task = input('Add a task: ')
        count += 1  # Increment task count
        
        if task.lower() == 'done':
            break  # Exit the loop if user is done
        elif task == '':
            print('You did not enter anything')
        
        elif task.lower() == 'delete':
            delete = int(input('What task do you want to delete'))
            del todo[1-delete]

        
        else:
            todo.append(f'Task{count}. {task}')  # Add the task to the list


    except ValueError:
        print('Error occurred, please try again.')
        
display_list()
print("Thank you! Here is your final To-Do List.")

