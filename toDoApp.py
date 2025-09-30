# toDoApp.py
# by Agustin, Chan, and Valencia of TN36
import os

tasks=[] #list to store the tasks thatll be listed

def clear_terminal():
    """
        Clearing of terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear') 

def wait_for_key():
    """
        Pause program until user inputs enter
    """
    input("\nPress Enter to continue...")
    clear_terminal()

def add_task(new_task):

    """ This is for adding a task within the list

    Args:
        new_task (str): append task to the list ; append is the most common adding within lists)
    """

    tasks.append(new_task)
    print("Task added successfully!")

def show_tasks():

    """Display tasks in the task list.

    If no tasks are present, a message is displayed that there are no tasks yet.
    """
    if len(tasks) == 0: #if task's list is empty/0, print no tasks added yet.
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks):    #else if it already have, loop through the list and print it
            print(f"[{i+1}] {task}")

def remove_task(): #removes a task from the list 

    """Removes a task from the task list.

    Prompts the user to select a numbered task,
    and handles invalid inputs and cancellation.
    """
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
    """Main program loop.

    Displays a menu for task management and executes user-selected actions:
        [1] Add Task
        [2] Show Tasks
        [3] Remove Task
        [4] Exit
    """
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
                print("Thank you for using the To-Do App. Goodbye!")
                break
            case _: #catch invalid inputs
                print("Invalid choice.")
main()
