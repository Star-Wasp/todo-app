# Importing functions from functions module
from functions import get_todos, write_todos
import time

print("Time stamp:")
today = time.strftime("%b.%d.%Y")
time_now = time.strftime("%H:%M:%S")
print(f"""
Today is: {today}
The time is: {time_now}""")

while True:
    # Get user input, strip and change to lower case
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action.startswith("add"):
        # Extracting to-do to add form user action
        todo = user_action[4:] + "\n"
        # Reading in the existing to-dos from the file into a todos list
        todos = get_todos()
        # Adding new to-do to the list and saving the updated to-dos list to the file
        todos.append(todo.capitalize())
        write_todos(todos)

    elif user_action.startswith("show"):
        # Opening todos file and reading to-dos into a list
        todos = get_todos()
        # Printing out todos list to the consol, numbered starting from 1
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip('\n')}")

    elif user_action.startswith("edit"):
        # Opening todos file and reading to-dos into a list
        todos = get_todos()
        try:
            # Getting number of to-do to edit and replacing with new to-do
            numer = int(user_action[5:])
            new_todo = input(f"Enter to-do to replace -{todos[numer-1]}: ").capitalize()
            todos[numer-1] = new_todo + "\n"
            # Writing updated todos list to the txt file
            write_todos(todos, )
        # Accounting for user error
        except ValueError:
            print("Invalid command. Please try again.")
            continue
        except IndexError:
            print("Invalid command. Please try again.")
            continue

    elif user_action.startswith("complete"):
        # Opening todos file and reading to-dos into a list
        todos = get_todos()
        try:
            # Getting number of the to-do that has been completed and removing it from list
            selected_todo = int(user_action[9:])
            completed_todo = todos[selected_todo-1]
            todos.pop(selected_todo-1)
            # Writing the updated todos list to the text file
            write_todos(todos, )
            # Printing message to consol to let the user know the to-do was removed successfully
            print(f"{completed_todo.strip("\n")} successfully completed!\n")
        # Accounting for user error
        except ValueError:
            print("Invalid command. Please try again.")
            continue
        except IndexError:
            print("Invalid command. Please try again.")
            continue

    # Breaking out of the loop once the user types "exit"
    elif user_action.startswith("exit"):
        break

    # Accounting for user error and letting them know the command is not valid
    else:
        print("Command not recognised")

# Printing farewell message once the user exits the program
print("See you next time!")
