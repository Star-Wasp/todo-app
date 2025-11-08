import functions
import FreeSimpleGUI as sg

# Row one
label = sg.Text("Type a to-do")
# Row two
input_box = sg.InputText(tooltip="Type a to-do")
add_button = sg.Button("Add")

# Making a window
window = sg.Window("__My to-do app__", layout=[[label], [input_box, add_button]])

window.read()
window.close()
