
tasks = []
int_tasks = int(input("how many Tasks would you like to input initially: "))
for i in range(int_tasks):
        task = input("input task: ")
        tasks.append(task)
while True:
        select = int(input("1. Add a new task \n2. Insert a task at a position \n3. Remove a task by name\n4. Remove a task by index\n5. Update a task\n6. View all tasks\n7. Sort tasks\n8. Reverse tasks\n9. Search for a task\n10. Task statistics\n11. Copy task list\n12. Clear all tasks\n13. Exit \n"))
        if select == 1:
                task = str(input("input new task: "))
                tasks.append(task)
        if select == 2:
                task = input("input new task: ")
                rank = int(input("input rank in order, 1 high: "))
                tasks.insert((rank-1),task)
        if select == 3:
                remove = str(input("what is the name of the task you would like to remove: "))
                if remove in tasks:
                    tasks.remove(remove)
                    print(f"removed {remove}")
                else:
                    print(f"{remove} not found in the list.")
        if select == 4:
                remove = int(input("input task number to remove: "))
                if remove <= len(tasks) and remove >= 1:
                       tasks.pop(remove-1)
                       print(f"task number {remove} is gone")
                else:
                       print(f"task number {remove} not found in the list.")
        if select == 5:
                change_num = int(input("input task number to change: "))
                changed = str(input("what would you like to change the task to: "))
                tasks[change_num] = changed
        if select == 6:
                print(tasks)
        if select == 7:
                tasks = sorted(tasks)
                print("list sorted alphabetically")
        if select == 8:
                tasks = reversed(tasks)
                print("tasks reversed")
        if select == 9:
                search_task = str(input("task to find: "))
                if search_task in tasks:
                    print(f"Found: {search_task}, rank in tasks is {(tasks.index(search_task))+1}")
                else:
                    print(f"{search_task} not found in the list.")
        if select == 10:
               print(f"total number of tasks is {len(tasks)}")
               print(f"the first task is {tasks[1]} \nthe last task is {tasks[-1]}")
        if select == 11:
               print(tasks)
               copy = tasks.copy()
               print(copy)
        if select == 12:
               yasure = input("you sure about that? yes/no ")
               if yasure == "yes":
                    tasks = tasks.clear()
               else:
                      print("ok i wont clear them ")
        if select == 13:
               break 
        else:
               print("pick valid number")

                
    #1. pop() removes via index number remove() uses the variable name
    #2. copy crates a challow copy not allowing the origonal to be changed
    #3. the variables are sorted alphabetically
    #4. each variable has an index number relating to the rank it is in the list

    

