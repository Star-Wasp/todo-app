def get_todos(filepath="todos.txt"):
    """ Takes filepath and opens file and returns list of todos """
    with open(filepath, "r") as file:
        local_todos = file.readlines()
    return local_todos

def write_todos(lst, filepath="todos.txt"):
    """ Takes list and filepath and writes list to file """
    with open(filepath, "w") as file:
       file.writelines(lst)