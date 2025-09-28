# toDoApp.py
# by Agustin, Chan, and Valencia of TN36
import os

tasks=[]

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def addTask(new_task):
    tasks.append(new_task)
    print("Task added successfully!")

def showTasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for i in range (len(tasks)):
            print(i+1, ".", tasks[i])

def removeTask(task_number):
    tasks.pop(task_number) 
    print("Task removed successfully!!")

def main():
    while True:
        print("[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Exit")
        
        choice = input("Enter choice: ")
        clearTerminal()
        
        match choice:
            case "1":
                new_task = input("Enter a task: ")
                addTask(new_task)
            case "2":
                showTasks()
            case "3":
                task_number = int(input("Enter a task number to be removed: "))
                removeTask(task_number)
            case "4":
                break
            case _:
                print("Invalid choice.")
main()
