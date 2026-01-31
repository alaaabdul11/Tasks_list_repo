import os

FILE_NAME = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")

def view_tasks():
    if not os.path.exists(FILE_NAME):
        print("No tasks found.")
        return

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")

def delete_task():
    if not os.path.exists(FILE_NAME):
        print("No tasks to delete.")
        return

    with open(FILE_NAME, "r") as f:
        tasks = f.readlines()

    view_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
    except (ValueError, IndexError):
        print("Invalid task number.")
        return

    with open(FILE_NAME, "w") as f:
        f.writelines(tasks)

def main():
    while True:
        choice = input(
            "\nA - Add Task\n"
            "V - View Tasks\n"
            "D - Delete Task\n"
            "E - Exit\n"
            "Choose: "
        ).lower()

        if choice == 'a':
            add_task()
        elif choice == 'v':
            view_tasks()
        elif choice == 'd':
            delete_task()
        elif choice == 'e':
            break
        else:
            print("Invalid choice.")

main()
