import json

print("Welcome to the cli task list!")
id_increment = 0

def add(task_name):
    global id_increment
    id_increment += 1

    task = {
        "id": id_increment,
        "description": task_name,
        "status": "todo"
    }

    print(f"{task["id"]} {task["description"]} ({task["status"]})")


add(input("Please enter your first task: "))

