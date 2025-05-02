from modules.functions import get_todos, set_todos
from FreeSimpleGUI import Window, Text, InputText, Button, Listbox, popup, theme
from time import strftime

theme("BlueMono")

clock = Text(strftime("%A, %Y-%m-%d %H:%M"), justification='center',
            expand_x=True,
            font=('Dejavu Serif', 24), key='-CLOCK-')
label = Text("Type in a to-do")
input_box = InputText(key='-NEW_TODO-', tooltip="Add new to-do")
add_button = Button("Add", key='-ADD_NEW_TODO-')
list_box = Listbox(values=get_todos(),
                   key='-TODOS-',
                   enable_events=True,
                   size=[45, 10])
done_button = Button("Done", key='-DONE_TODO-')
quit_button = Button("Quit", key='-QUIT-')

window = Window('To-do App', 
                layout=[[clock], [label], [input_box, add_button], [list_box, done_button], [quit_button]], 
                font=('Dejavu Serif', 18))


while True:
    event, values = window.read(timeout=60000)
    window['-CLOCK-'].update(strftime("%A, %Y-%m-%d %H:%M"))
    match event:
        case '-ADD_NEW_TODO-':
            new_todo = values['-NEW_TODO-'].strip()
            if new_todo != '':
                todos = get_todos()
                try:
                    selected_todo = values['-TODOS-'][0]
                    index = todos.index(selected_todo)
                    todos[index] = new_todo
                except IndexError:
                    todos.append(new_todo)
                
                set_todos(todos)
                window['-NEW_TODO-'].update('')
            window['-TODOS-'].update(get_todos())
            window['-ADD_NEW_TODO-'].update("Add")

        case '-TODOS-':
            selected_todo = values['-TODOS-'][0]
            window['-NEW_TODO-'].update(selected_todo)
            window['-ADD_NEW_TODO-'].update("Update")

        case '-DONE_TODO-':
            try:
                selected_todo = values['-TODOS-'][0]
                todos = get_todos()
                index = todos.index(selected_todo)
                todos.pop(index)
                set_todos(todos)
                window['-TODOS-'].update(get_todos())
                window['-NEW_TODO-'].update('')
                window['-ADD_NEW_TODO-'].update("Add")
            except IndexError:
                popup('Please select a to-do item', font=('Dejavu Serif', 18))
        
        case '-QUIT-':
            break
            

window.close()

