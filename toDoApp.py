# toDoApp.py

tasks=[]

def addtask(task) :
  tasks.append(task)
  print("Task added successfully!")

def showTasks( ):
    if len(tasks)==0 :
      print("No tasks added yet.")
    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("Task removed successfully!!")

def main():
    while True:
        print("[1] Add Task")
        print("[2] Show Tasks")
        print("[3] Remove Task")
        print("[4] Exit")
        ch = input("Enter choice : ")
        if ch=="1":
            t = input("Enter a task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("Enter a task number to be removed : "))
            removetask(n)   
        elif ch=="4":
            break
        else:
            print("Invalid choice.")
main()
