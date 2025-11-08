FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Takes filepath and opens file and returns list of todos """
    with open(filepath, "r") as file:
        local_todos = file.readlines()
    return local_todos

def write_todos(lst, filepath=FILEPATH):
    """ Takes list and filepath and writes list to file """
    with open(filepath, "w") as file:
       file.writelines(lst)