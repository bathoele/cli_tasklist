import datetime
import os
import json
import re

print('Welcome to the task cli app!')

task_list = []
cmd_list = ["add", "delete", "update", "list", "mark-in-progress", "mark-done"]
space_list = []
for word in cmd_list:
    space_list.append(f"{word} ")

# if file exists, load \json to task_list
if os.path.exists("best_task_list.json"):
    with open("best_task_list.json") as f:
        task_list = json.load(f)
        f.close()

def main():
    def check_input(the_put):
        if the_put.startswith(tuple(cmd_list)):
            if the_put.startswith(tuple(space_list)) or the_put.replace(" ", "") == "list":
                # check for add, delete, and update
                print(the_put)

                if the_put.startswith("add "):
                    if re.search(r"^add [\"'][a-zA-Z\s]+[\"']", the_put):
                        pass
                    else:
                        print("Please put your task name in quotes!")
                elif the_put.startswith("delete " or "mark-in-progress " or "mark-done "):
                    pass
                elif the_put.startswith("update "):
                    pass
                elif the_put == "list to-do" or "list done" or "list in-progress":
                    pass



            else:
                print("Please format the command correctly")
        else:
            print("Please use one of the command keywords.")

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
        task_id = len(task_list) + 1

        task_list.append({
            "id": task_id,
            "description": task_input,
            "status": "to-do",
            "createdAt": datetime.datetime.now(),
            "updatedAt": False,
        })
        print(f"{task_input} (ID: {task_list[task_id - 1]["id"]}) was added to the list!")

    def update():
        global task_list
        nonlocal cmd_input
        task_num = cmd_input[7]

        if task_num.isdigit():
            input_list = cmd_input.partition(task_num)
            new_desc = input_list[2].replace('"', '').lstrip()
            task_index = int(task_num) - 1
            task_list[task_index]["description"] = new_desc
            task_list[task_index]["updatedAt"] = datetime.datetime.now()

    #       update \json file

    def mark_progress(cmd, task_num):
        global task_list
        task_index = int(task_num) - 1
        if cmd == "mark-in-progress":
            task_list[task_index]["status"] = "in-progress"
        else:
            task_list[task_index]["status"] = "done"

    def delete(task_num):
        global task_list
        for task in task_list:
            if str(task["id"]) == task_num:
                task_list.remove(task)
                print(f"Task '{task["description"]}' was removed!")

    def list_tasks():
        global task_list

        def display(status):
            list_absent = True
            for item in task_list:
                if item["status"] == status:
                    list_absent = False
                    print(f"{item['id']} {item['description']} ({item['status']})")
            if list_absent:
                print(f"Sorry, there are no '{status}' tasks!")

        if cmd_input.rstrip(" ") == "list":
    #       load and display \json file
            for task in task_list:
                print(f"{task['id']} {task['description']} ({task['status']})")
        else:
            match cmd_input.split()[1]:
                case "done":
                    display("done")
                case "to-do":
                    display("to-do")
                case "in-progress":
                    display("in-progress")

    def handle_cmd():
        nonlocal cmd_input

        if cmd_input.startswith("add ") and cmd_input.endswith('"'):
            add()
        if cmd_input == "list" or cmd_input.startswith("list "):
            list_tasks()
        if cmd_input.startswith("delete ") and cmd_input[7].isdigit() and cmd_input.endswith(cmd_input[7]):
            delete(cmd_input[7])
        if cmd_input.startswith("update ") and cmd_input[7].isdigit() and cmd_input[8].isspace():
            update()
        if cmd_input.startswith(("mark-in-progress", "mark-done")) and cmd_input[-1].isdigit():
            input_list = cmd_input.split()
            mark_progress(input_list[0], input_list[1])

        sort_ids()

        # update the file with the saved task_list
        with open("best_task_list.json", "w") as g:
            g.write(json.dumps(task_list, indent=4, default=str))
            g.close()

        cmd_input = input()
        check_input(cmd_input)
        handle_cmd()

    if True:
        check_input(cmd_input)
        handle_cmd()

if __name__ == '__main__':
    main()