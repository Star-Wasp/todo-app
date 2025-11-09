import functions
import FreeSimpleGUI as sg
import time

# Constants
FONT = ('Input Mono', 16)

# Row one
label = sg.Text("Type a to-do")
clock = sg.Text("", key="Clock")
# Row two
input_box = sg.InputText(tooltip="Type a to-do:", key="to-do", font=FONT)
add_button = sg.Button("Add")
# Row three
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
# Row four
exit_button = sg.Button("Exit")

# LAYOUT
layout = [[label, clock],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

# Making a window
window = sg.Window(title="__My to-do app__",
                   layout=layout,
                   font=FONT)

while True:
    event, values = window.read(timeout=10)
    window["Clock"].update(value=time.strftime("%H:%M:%S %d/%m/%Y"))
    match event:
        # Allowing user to add a to-do
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(todos)

        # Allowing user to edit existing to-do
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["to-do"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do to edit!", text_color="dark blue", font=FONT)

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do to complete!", text_color="dark blue", font=FONT)

        case "Exit":
            break

        # Placing current selection in input box
        case "todos":
            window["to-do"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()
