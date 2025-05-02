from modules.functions import get_todos, set_todos
from FreeSimpleGUI import Window, Text, InputText, Button, Listbox

label = Text("Type in a to-do")
input_box = InputText(key='-NEW_TODO-', tooltip="Add new to-do")
add_button = Button("Add", key='-ADD_NEW_TODO-')
list_box = Listbox(values=get_todos(),
                   key='-TODOS-',
                   enable_events=True,
                   size=[45, 10])
edit_button = Button("Edit", key='-EDIT_TODO-')
quit_button = Button("Quit", key='-QUIT-')

window = Window('To-do App', 
                layout=[[label], [input_box, add_button], [list_box, edit_button], [quit_button]], 
                font=('Dejavu Serif', 18))


while True:
    event, values = window.read()
    match event:
        case '-ADD_NEW_TODO-':
            new_todo = values['-NEW_TODO-'].strip()
            if new_todo != '':
                todos = get_todos()
                todos.append(new_todo)
                set_todos(todos)
                window['-NEW_TODO-'].update('')
            window['-TODOS-'].update(get_todos())

        case '-TODOS-':
            selected_todo = values['-TODOS-'][0]
            window['-NEW_TODO-'].update(selected_todo)

        case '-EDIT_TODO-':
            todos = get_todos()
            index = todos.index(selected_todo)
            new_todo = values['-NEW_TODO-'].strip()
            if new_todo != '':
                todos[index] = new_todo
                set_todos(todos)
                window['-NEW_TODO-'].update('')
            window['-TODOS-'].update(get_todos())
        
        case '-QUIT-':
            break
            

window.close()

