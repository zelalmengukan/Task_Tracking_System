# List Definitions
tasks = []
completed_tasks = []


def add_task():
    """Adds a new task received from the user to the list."""
    new_task = input("\nEnter the task to add: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"Task '{new_task}' added.")
    else:
        print("Error: Task cannot be empty.")


def list_tasks():
    """Prints all current tasks to the screen with their numbers."""
    print("\n--- CURRENT TASKS ---")
    if not tasks:
        print("There are no tasks in the list.")
    else:
        for index, task in enumerate(tasks):
            print(f"[{index}] {task}")


def complete_task():
    """Moves the selected task to the completed tasks list."""
    if not tasks:
        print("\nNo tasks to complete.")
        return

    list_tasks()

    try:
        choice = int(
            input("\nEnter the number of the completed task: ").strip()
        )
        if 0 <= choice < len(tasks):
            completed = tasks.pop(choice)
            completed_tasks.append(completed)
            print(f"Task '{completed}' marked as completed.")
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a numeric value.")


def list_completed_tasks():
    """Displays all completed tasks."""
    print("\n--- COMPLETED TASKS ---")
    if not completed_tasks:
        print("There are no completed tasks.")
    else:
        for index, task in enumerate(completed_tasks, 1):
            print(f"{index}. {task}")


def main_menu():
    """Application main menu loop."""
    while True:
        print("\n" + "=" * 30)
        print("     TASK TRACKING SYSTEM")
        print("=" * 30)
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Show Completed Tasks")
        print("5. Exit")

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            list_completed_tasks()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a value between 1 and 5.")


if __name__ == "__main__":
    main_menu()
