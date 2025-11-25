import argparse

# In-memory task store
tasks = []

def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    return task

def list_tasks():
    return tasks

def update_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return None

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI")

    parser.add_argument("command", choices=["add", "list", "update", "delete"])
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        if not args.title:
            print("Please provide a title using --title")
        else:
            task = add_task(args.title)
            print(f"Task added: {task['title']}")

    elif args.command == "list":
        all_tasks = list_tasks()
        if not all_tasks:
            print("No tasks found")
        for task in all_tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f"{task['id']}. {task['title']} - {status}")

    elif args.command == "update":
        if not args.id:
            print("Please provide an ID using --id")
        else:
            updated = update_task(args.id)
            if updated:
                print("Task marked as completed")
            else:
                print("Task not found")

    elif args.command == "delete":
        if not args.id:
            print("Please provide an ID using --id")
        else:
            deleted = delete_task(args.id)
            if deleted:
                print("Task deleted")
            else:
                print("Task not found")


if __name__ == "__main__":
    main()
