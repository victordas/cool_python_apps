from modules.functions import get_todos, set_todos
from FreeSimpleGUI import Window, Text, InputText, Button

label = Text("Type in a to-do")
input_box = InputText(tooltip="Enter to-do")
add_button = Button("Add")

window = Window('To-do App', layout=[[label], [input_box, add_button]])

window.read()
window.close()

