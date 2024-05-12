# TO DO LIST USING PYTHON

def task():
    tasks = []
    print("Welcome to the Task Management System")

    total_task = int(input("How many task you want to add = "))

    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i}")
        tasks.append(task_name)

    print(f"Today's task are\n{tasks}")

    while True:
        operation = int(input('Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop'))
        if operation == 1:
            add = input("Enter Task to add in list")
            tasks.append(add)
            print(f"Task{add} has been added successfully")
        elif operation == 2:
            update = input("Enter the task you want to update")
            if update in tasks:
                up = input("Enter new task")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f"Updated task {up}")
        elif operation == 3:
            del_value = input("Which task you want to delete")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task{del_value} has been removed from the list ")
        elif operation == 4:
            print(f"Total task {tasks}")
        elif operation == 5:
            print("CLOSING THE PROGRAM")
            break
task()