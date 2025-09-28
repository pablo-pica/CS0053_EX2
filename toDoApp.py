# toDoApp.py
# by Agustin, Chan, and Valencia of TN36
import os

tasks=[]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def wait_for_key():
    input("Press Enter to continue...")
    clear_terminal()
    
def add_task(new_task):
    tasks.append(new_task)
    print("Task added successfully!")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for i in range (len(tasks)):
            print(i+1, ".", tasks[i])

def remove_task(task_number):
    if task_number < 0 or task_number > len(tasks):
        print("Invalid task number.")
        return
    
    print("Task to be removed:", tasks[task_number - 1])
    print("Are you sure you want to remove this task? (y/n)")
    confirmation = input().lower()
    
    if confirmation == 'y':
        tasks.pop(task_number - 1)
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
        
        choice = input("Enter choice: ")
        clear_terminal()
        
        match choice:
            case "1":
                new_task = input("Enter a task: ")
                add_task(new_task)
            case "2":
                show_tasks()
                wait_for_key()
            case "3":
                task_number = int(input("Enter a task number to be removed: "))
                remove_task(task_number)
                wait_for_key()
            case "4":
                break
            case _:
                print("Invalid choice.")
main()
