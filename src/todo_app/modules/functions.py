import subprocess

def get_todos():
    """
    Read a text file and return list of to-do items
    """
    try:
        with open('src/todo_app/todos.txt', 'r') as file:
            todos = file.readlines()
            return todos
    except:
        return []
    

def set_todos(todos):
    """
    Write a list of to-do items to the file
    """
    with open('src/todo_app/todos.txt', 'w') as file:
        file.writelines(todos)


def open_in_windows_browser(url):
    try:
        subprocess.run(["powershell.exe", "Start-Process", url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open browser: {e}")