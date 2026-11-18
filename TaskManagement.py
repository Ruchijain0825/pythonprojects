def task():
    tasks = []
    print("---Welcome to the task management app---")
    total_task=int(input("Enter how many task you want to add = "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    print("Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task to add = ")
            task.append(add)
            print(f" Task {task} has been added successfully")
        elif operation == 2:
            Updated_val = input("Enter the task to be updated = ")
            if Updated_val in tasks:
                up = input("Enter new value = ")
                ind = tasks.index(Updated_val)
                tasks[ind] = up
                print(f"updated task {up}")
        elif operation == 3:
            del_value = input("which task is need to be deleted = ")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value} has been deleted")

        elif operation == 4:
            print("Total tasks = {tasks}")
        else:
            print("invalid input")