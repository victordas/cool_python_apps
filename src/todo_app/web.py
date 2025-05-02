from streamlit import title, subheader, checkbox, text_input, session_state, rerun
from modules.functions import get_todos, set_todos

def add_todo():
    todo = session_state['-NEW_TODO-'].strip()
    if todo != "":
        todos.append(todo)
        set_todos(todos)
        session_state['-NEW_TODO-'] = ""


todos = get_todos()

title('To-do App')
subheader("My personal productivity app")

for index, todo in enumerate(todos):
    checked = checkbox(todo, key=f"todo_{index}")
    if checked:
        todos.pop(index)
        set_todos(todos)
        rerun()

text_input(label="", 
           placeholder="Add a new to-do", 
           on_change=add_todo, 
           key='-NEW_TODO-')