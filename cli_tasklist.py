

task_list = []
increment_id = len(task_list)

def main():
    cmd_input = input("Give me first input! ")

    def add():
        global increment_id
        increment_id += 1
        task_input = cmd_input.replace('add "', "", 1)
        task_input = task_input.replace('"', "")

        task_list.append({
            "id": increment_id,
            "description": task_input,
            "status": "to-do",
        })
        # add task details to \json file

        print(f"{task_input} was added to the list!")

    def list_tasks():
        if cmd_input.replace(" ", "") == "list":
            print("listing all items")
    #       load and display json file
            for task in task_list:
                print(f"{task['id']}. {task['description']}")

    def handle_cmd():
        nonlocal cmd_input
        if cmd_input.startswith("add ") and cmd_input.endswith('"'):
            add()
        if cmd_input.startswith("list"):
            list_tasks()
        cmd_input = input("Give me new input! ")
        handle_cmd()

    if True:
        handle_cmd()


if __name__ == '__main__':
    main()