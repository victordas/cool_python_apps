from modules.functions import get_todos, set_todos
from time import strftime

print(f"\nIt is {strftime("%A, %Y-%m-%d %H:%M:%S")}\n")

while True:
    user_action = input("Type A to add a new todo" \
    "\nType S to show current items in todos" \
    "\nType E to edit a todo item" \
    "\nType R to remove a todo item" \
    "\nType Q to quit the application" \
    "\n\nEnter an option: ").strip().upper()
    
    match user_action:
        case 'A':
            while True:
                todos = get_todos()
                todo = input("\n\nEnter a todo (Type 'Q' when done): ")
                if todo.strip().upper() == 'Q':
                    break;
                todos.append(todo)
                set_todos(todos)
                
        case 'S':
            print("\n")
            
            todos = get_todos()
            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip("\n")}")

            print("\n")

        case 'Q':
            break

        case 'E':
            todos = get_todos()
            serial_number = int(input("\n\nEnter the item number to edit: ")) - 1
            if len(todos) > serial_number > -1:
                current_todo = todos[serial_number].strip("\n")
                new_todo = input(f"\nEdit todo ({current_todo}): ") + "\n"
                todos[serial_number] = new_todo
                set_todos(todos)
            else:
                print("\nWe can't find the item")

        case 'R':
            todos = get_todos()
            serial_number = int(input("\n\nEnter the item number to remove: ")) - 1
            if len(todos) > serial_number > -1:
                removed_todo = todos.pop(serial_number)
                print(f"\nRemoved todo: ({removed_todo})")               
                set_todos(todos)

            else:
                print("\nWe can't find the item")

        case _:
            print(f"\n{'=' * 23}\nInvalid option. Retry!!\n{'=' * 23}\n")

print("See ya!")
