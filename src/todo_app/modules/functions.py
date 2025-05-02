import subprocess

FILE_PATH='../todo_app/todos.txt'

def get_todos():
    """
    Read a text file and return list of to-do items
    """
    try:
        with open(FILE_PATH, 'r') as file:
            todos = file.readlines()
            return [todo.strip("\n") for todo in todos]
    except:
        return []
    

def set_todos(todos):
    """
    Write a list of to-do items to the file
    """
    with open(FILE_PATH, 'w') as file:
        file.writelines([todo + "\n" for todo in todos])


def open_in_windows_browser(url):
    try:
        subprocess.run(["powershell.exe", "Start-Process", url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open browser: {e}")