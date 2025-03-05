
import time

TXT_FILEPATH = "todos.txt"


def show_commands(dic: dict):
    """Prints a formatted dictionary of commands. Takes dict"""
    print("--------------- COMMANDS ---------------")
    for key, value in dic.items():
        print(f"{key} | {value}")
    print("")


def get_todo_list(filepath=TXT_FILEPATH):
    """Returns a LIST type of the unformatted todos in a text file. If no such file exists, create one
     and return an empty list. """
    try:
        with open(filepath, "r") as local_file:
            local_todos = local_file.readlines()
            local_todos = [i.strip(f"{local_todos.index(i)+1}.").strip() for i in local_todos]
    except FileNotFoundError:
        with open(filepath, "w") as local_file:
            pass
        return []
    return local_todos


def show_formatted_list(lst):
    """Prints a formatted to-do list. Takes list argument."""
    print("--------------- TODO LIST ---------------")
    for i, v in enumerate(lst):
        print(f"{i+1}. {v}")
    print("")


def save_txt_file(lst, filepath=TXT_FILEPATH):
    """Takes a list type and saves it into a formatted to-do list txt file."""
    with open(filepath, "w") as local_file:
        for i, v in enumerate(lst):
            local_file.write(f"{(i + 1)}. {v}\n")


def get_day_info():
    return f"{time.strftime("%A | %B %d, %Y | %I:%M %p ")}"


if __name__ == "__main__":
    print(get_todo_list())
