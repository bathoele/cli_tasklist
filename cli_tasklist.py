import argparse

FILENAME = "todo.txt"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage your to-do list")
    parser.add_argument("action", choices=["add", "list", "done"], help="Action to perform")
    parser.add_argument("--item-text", help="Text of the item to add")
    parser.add_argument("--item-number", type=int, help="Number of the item to mark done")
    args = parser.parse_args()

    if args.action == "add":
        # add_item(args.item_text)
    elif args.action == "done":
        # mark_item_done(args.item_number)
    elif args.action == "list":
        # list_items()