

task_list = []
increment_id = 0

def main():

    cmd_input = input("Give me task: ")

    def add():
        task_input = cmd_input.replace('add "', "", 1)
        task_input = task_input.replace('"', "")

        task_list.append({
            "id": increment_id + 1,
            "description": task_input,
        })
        # add task description to \json file

        print(f"{task_input} was added to the list!")

    def list_tasks():
        if cmd_input.replace(" ", "") == "list":
            print("listing items")

    def handle_cmd():
        if cmd_input.startswith("add ") and cmd_input.endswith('"'):
            add()
        if cmd_input.startswith("list"):
            list_tasks()

    if True:
        handle_cmd()

if __name__ == '__main__':
    main()