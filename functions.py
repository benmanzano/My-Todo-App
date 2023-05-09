FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of items
    found in the file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):  # with the = , filepath now has a default parameter
    # value, so you can get rid of that specified word in later call
    """ Write the item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_argument)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
