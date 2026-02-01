#  Task List (To-Do Application)

##  Description
This is a Python command-line application that allows the user to manage a list of tasks.
The user can add, view, delete tasks, or exit the program using a simple menu.

##  Technologies Used
- Python 3
- File Handling
- os module

##  How It Works
- The program displays a menu and asks the user to choose an option:
  - **A** → Add a new task
  - **V** → View all tasks
  - **D** → Delete a task
  - **E** → Exit the program
- Tasks are stored in a text file.
- Error handling is implemented using `try / except` to prevent crashes from invalid input.

##  Function Explanation

### `main()`
- Runs the program inside a `while` loop.
- Displays the menu and waits for user input.
- Uses conditional statements (`if / elif`) to call the correct function.
- Stops the program when the user chooses **E (Exit)**.

### `add_task()`
- Asks the user to enter a new task.
- Opens the file in append mode.
- Saves the task to the file.

### `view_tasks()`
- Checks if the task file exists.
- Reads all tasks into a list.
- Displays the tasks in a numbered and clean format.

### `delete_task()`
- Checks if the task file exists.
- Reads all tasks into a list.
- Calls `view_tasks()` so the user can see available tasks.
- Asks the user for the task number to delete.
- Uses `try / except` to handle `ValueError` and `IndexError`.
- Removes the selected task using `pop()`.
- Writes the updated task list back to the file.

##  How to Run the Program
1. Make sure Python is installed.
2. Run the program using:
   ```bash
   python Tasks_list_repo.py

## Example Output:
A - Add Task
V - View Tasks
D - Delete Task
E - Exit
Choose: A
Enter new task: Send the Email

Choose: V
1. Send the Email
2. Call Mr. Robert

Choose: D
1. Send the Email
2. Call Mr. Robert
Enter task number to delete: 1

Choose: E



