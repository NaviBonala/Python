# Step 1: Create an empty list to store tasks
tasks = []

while True:
    # Step 2: Show menu
    print("\n--- To-Do List Menu ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

    # Step 3: Get user choice
    choice = input("Choose an option (1-4): ")

    # Step 4: Perform actions
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks yet.")
        else:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("⚠️ No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"❌ Removed task: {removed}")
                else:
                    print("🚫 Invalid task number.")
            except ValueError:
                print("🚫 Please enter a number.")

    elif choice == "4":
        print("👋 Goodbye! Stay productive!")
        break

    else:
        print("❗ Please choose a valid option (1-4).")
