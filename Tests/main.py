import os


todo = []
count = 0

def display_list():
    print(f'list: {todo}')
    


print('Welcome to the to-do list')
print('When all tasks are added type \'done\'')


while True:
    try:
        
        display_list()
        
        task = input('Add a task: ')
        count += 1
        todo.append(f'{count}:{task}')
       
    

        if task.lower() == 'done':
            break
            display_list(count, task)
    
    except ValueError:
        print('Error occured, please try again')
