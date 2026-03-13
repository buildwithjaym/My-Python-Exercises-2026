tasks =[]

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        task=input("Enter Task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks: ")

        for i, task in enumerate(tasks):
            print(i + 1, "-", task)
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")