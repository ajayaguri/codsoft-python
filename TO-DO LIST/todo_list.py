import json
from tabulate import tabulate
from datetime import datetime, timedelta

tasks = []
update_history = []

def add_task():
    count = int(input("Enter the number of tasks to add: "))
    for _ in range(count):
        task_name = input("Enter task name: ")
        
        while True:
            due_date_input = input("Enter due date (dd-mm-yyyy): ")
            try:
                # Convert the input date to the required format
                due_date = datetime.strptime(due_date_input, "%d-%m-%Y").strftime("%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date format. Please use dd-mm-yyyy.")
        
        current_date = datetime.now().strftime("%d-%m-%Y")
        task = {'name': task_name, 'due_date': due_date, 'status': 'Pending', 'current_date': current_date}
        tasks.append(task)
        print("Task added successfully.")
        record_update(f"Added task '{task_name}' with due date {due_date}.")

def calculate_time_left(due_date, status):
    due_date_obj = datetime.strptime(due_date, "%d-%m-%Y")
    current_date_obj = datetime.now()

    if status.lower() == 'completed':
        return "Task has been completed"

    if due_date_obj.date() == current_date_obj.date():
        return "Today"

    if due_date_obj.date() == (current_date_obj + timedelta(days=1)).date():
        return "Tomorrow"

    time_left = (due_date_obj - current_date_obj).days
    if time_left < 0:
        return f"You are {-time_left} days late"
    
    return f"{time_left} days"

def list_tasks(status=None):
    if status:
        filtered_tasks = [task for task in tasks if task['status'].lower() == status.lower()]
    else:
        filtered_tasks = tasks
    
    if filtered_tasks:
        table = []
        for i, task in enumerate(filtered_tasks, start=1):
            time_left = calculate_time_left(task['due_date'], task['status'])
            table.append([i, task['name'], task['current_date'], task['due_date'], time_left, task['status']])
        print(tabulate(table, headers=["ID", "Task Name", "Current Date", "Due Date", "Time Left", "Status"], tablefmt="grid"))
    else:
        print(f"No tasks found for status: {status if status else 'All'}.")

def update_tasks():
    list_tasks()
    task_ids = input("Enter task IDs to update (comma-separated): ").split(',')
    task_ids = [int(task_id.strip()) - 1 for task_id in task_ids]
    
    for task_id in task_ids:
        if 0 <= task_id < len(tasks):
            old_task = tasks[task_id].copy()
            print(f"Updating task ID {task_id + 1}...")
            print("Leave blank if you do not want to update a field.")
            
            new_name = input(f"Enter new task name (current: {tasks[task_id]['name']}): ")
            if new_name:
                tasks[task_id]['name'] = new_name
            
            while True:
                new_due_date_input = input(f"Enter new due date (dd-mm-yyyy) (current: {tasks[task_id]['due_date']}): ")
                if new_due_date_input == "":
                    break
                try:
                    tasks[task_id]['due_date'] = datetime.strptime(new_due_date_input, "%d-%m-%Y").strftime("%d-%m-%Y")
                    break
                except ValueError:
                    print("Invalid date format. Please use dd-mm-yyyy.")
            
            new_status = input(f"Enter new status (Pending/Completed) (current: {tasks[task_id]['status']}): ")
            if new_status:
                new_status = new_status.capitalize()
                if new_status in ['Pending', 'Completed']:
                    tasks[task_id]['status'] = new_status
                    # If status is updated to 'Completed', set due date to current date
                    if new_status.lower() == 'completed':
                        tasks[task_id]['due_date'] = datetime.now().strftime("%d-%m-%Y")
                else:
                    print("Invalid status. Status must be 'Pending' or 'Completed'.")
            
            new_task = tasks[task_id]
            record_update(f"Updated task ID {task_id + 1}: Before - {old_task}, After - {new_task}")
            print(f"Task ID {task_id + 1} updated successfully.")
        else:
            print(f"Invalid task ID: {task_id + 1}. Skipping update for this ID.")

def delete_task():
    list_tasks()
    task_id = int(input("Enter task ID to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        task_data = tasks.pop(task_id)
        record_update(f"Deleted task ID {task_id + 1}: {task_data}")
        print("Task deleted successfully.")
    else:
        print("Invalid task ID.")

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    print("Tasks saved successfully.")

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded successfully.")
    except FileNotFoundError:
        print("No saved tasks found.")

def record_update(update_message):
    if len(update_history) >= 4:
        update_history.pop(0)
    update_history.append(update_message)

def view_update_history():
    if update_history:
        print("\nLast 4 Updates:")
        table = []
        for update in update_history:
            table.append([update])
        print(tabulate(table, headers=["Update History"], tablefmt="grid"))
    else:
        print("No update history available.")

def menu():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task(s)")
        print("2. Update Task(s)")
        print("3. Delete Task")
        print("4. List All Tasks")
        print("5. List Pending Tasks")
        print("6. List Completed Tasks")
        print("7. Save Tasks")
        print("8. Load Tasks")
        print("9. View Last 4 Updates")
        print("10. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            update_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            list_tasks(status='Pending')
        elif choice == '6':
            list_tasks(status='Completed')
        elif choice == '7':
            save_tasks()
        elif choice == '8':
            load_tasks()
        elif choice == '9':
            view_update_history()
        elif choice == '10':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
