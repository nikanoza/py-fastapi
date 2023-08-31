import requests

class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, task):
        return requests.post(TaskClient.BASE_URL, json=task).json()

    def get_task(self, task_id):
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def get_all_tasks(self):
        return requests.get(TaskClient.BASE_URL).json()

    def update_task(self, task_id, new_task):
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=new_task).json()

    def delete_task(self, task_id):
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()

def print_task(task):
    print(f"ID: {task['id']}, Title: {task['title']}, Completed: {task['completed']}")

def main():
    client = TaskClient()

    while True:
        print("\nMenu:")
        print("1. Create Task")
        print("2. Read Task")
        print("3. Read All Tasks")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = int(input("Enter ID: "))
            title = input("Enter Title: ")
            completed = input("Enter Completed (True/False): ").capitalize()
            task = {"id": id, "title": title, "completed": completed == "True"}
            client.create_task(task)
            print("Task created successfully!")

        elif choice == "2":
            task_id = int(input("Enter Task ID: "))
            task = client.get_task(task_id)
            print_task(task)

        elif choice == "3":
            tasks = client.get_all_tasks()
            for task in tasks:
                print_task(task)

        elif choice == "4":
            task_id = int(input("Enter Task ID: "))
            task = client.get_task(task_id)
            print("Current task:")
            print_task(task)
            new_title = input("Enter New Title: ")
            new_completed = input("Enter New Completed (True/False): ").capitalize()
            new_task = {"id": task_id, "title": new_title, "completed": new_completed == "True"}
            client.update_task(task_id, new_task)
            print("Task updated successfully!")

        elif choice == "5":
            task_id = int(input("Enter Task ID: "))
            task = client.get_task(task_id)
            print("Task to be deleted:")
            print_task(task)
            confirm = input("Are you sure you want to delete this task? (y/n): ").lower()
            if confirm == "y":
                deleted_task = client.delete_task(task_id)
                print("Task deleted successfully!")
                print_task(deleted_task)

        elif choice == "6":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()