import functions
import FreeSimpleGUI as sg

# Constants
FONT = ('Input Mono', 16)

# Row one
label = sg.Text("Type a to-do")
# Row two
input_box = sg.InputText(tooltip="Type a to-do:", key="to-do", font=FONT)
add_button = sg.Button("Add")

# Making a window
window = sg.Window(title="__My to-do app__",
                   layout=[[label], [input_box, add_button]],
                   font=FONT)

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["to-do"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            pass
        case "Complete":
            pass
        case "Show":
            pass
        case sg.WIN_CLOSED:
            break

window.close()
