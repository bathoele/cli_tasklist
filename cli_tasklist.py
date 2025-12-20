

def main():

    cmd_input = input("Give me task: ")

    def add():
        task_input = cmd_input.replace('add "', "", 1)
        task_input = task_input.replace('"', "")

        # add task description to \json file

        print(f"{task_input} was added to the list!")

    def handle_cmd():
        if cmd_input.startswith("add ") and cmd_input.endswith('"'):
            add()

    if True:
        handle_cmd()

if __name__ == '__main__':
    main()