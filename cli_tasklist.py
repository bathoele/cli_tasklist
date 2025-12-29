

task_list = []

def main():
    cmd_input = input("Give me first input! ")

    def sort_ids():
        global task_list
        increment_id = 0
        for task in task_list:
            task["id"] = increment_id + 1
            increment_id += 1


    def add():
        global task_list
        task_input = cmd_input.replace('add "', "", 1)
        task_input = task_input.replace('"', "")

        task_list.append({
            "id": len(task_list) + 1,
            "description": task_input,
            "status": "to-do",
        })
        # add task details to \json file

        print(f"{task_input} was added to the list!")

    def delete(task_num):
        global task_list
        for task in task_list:
            if str(task["id"]) == task_num:
                task_list.remove(task)
                print(f"Task '{task["description"]}' was removed!")

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
        if cmd_input.startswith("delete") and cmd_input[-1].isdigit():
            delete(cmd_input[-1])

        sort_ids()
        cmd_input = input("Give me new input! ")
        handle_cmd()

    if True:
        handle_cmd()


if __name__ == '__main__':
    main()