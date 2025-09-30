# toDoApp.py
# by Agustin, Chan, and Valencia of TN36
import os

tasks=[] #list to store the tasks thatll be listed

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') #clearing of terminal screen
    
def wait_for_key(): #pause program until user inputs enter
    input("\nPress Enter to continue...")
    clear_terminal()
    
def add_task(new_task): #adds new task to the list
    tasks.append(new_task) #append task to the list ; append is the most common adding within lists)
    print("Task added successfully!")

def show_tasks(): #displays all tasks
    if len(tasks) == 0: #if task's list is empty/0, print no tasks added yet.
        print("No tasks added yet.")
    else:
        for i in range (len(tasks)): #else if it already have, loop through the list and print it
            print(f"[{i+1}] {tasks[i]}")

def remove_task(): #removes a task from the list 
    if len(tasks) == 0: #if list is 0/empty, print no task to remove.
        print("No tasks to remove.")
        return
    show_tasks() #show task for user to pick what to remove
    
    while True: #ask until valid input is entered
        user_input = input("\nEnter a task number to be removed: ")

        try:
            if not user_input.strip(): #prevent empty input
                print("Input cannot be empty. Please enter a number.")
                continue
            task_number = int(user_input) #convert input to int
            if task_number < 1 or task_number > len(tasks):
                print("Invalid task number. Please enter a number between 1 and", len(tasks))
                continue
            break #if valid input, exit loop
            
        except ValueError: #if input not a number
            print("Invalid input. Please enter a whole number.")
            continue

    print("Task to be removed:", tasks[task_number - 1])
    print("Are you sure you want to remove this task? (y/n)")
    confirmation = input().lower()
    
    if confirmation == 'y':
        tasks.pop(task_number - 1) #remove chosen task by popping
        print("Task removed successfully!")
    elif confirmation == 'n':
        print("Task removal cancelled.")
    else:
        print("Invalid input. Task removal cancelled.")

def main():
    while True:
        print("[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Exit")
        
        choice = input("Enter choice: ") #ask user for option
        clear_terminal()
        
        match choice:
            case "1": #add a task
                new_task = input("Enter a task: ")
                add_task(new_task)
            case "2": #show tasks
                show_tasks()
                wait_for_key()
            case "3": #remove a task
                remove_task()
                wait_for_key()
            case "4": #exit program
                break
            case _: #catch invalid inputs
                print("Invalid choice.")
main()
