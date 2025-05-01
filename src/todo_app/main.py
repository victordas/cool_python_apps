todos = []

while True:
    user_action = input("Type A to add a new todo" \
    "\nType S to show current items in todos" \
    "\nType Q to quit the application" \
    "\nType E to edit a todo item" \
    "\n\nEnter an option: ").strip().upper()
    
    match user_action:
        case 'A':
            todo = input("\n\nEnter a todo: ")
            todos.append(todo.capitalize())
        case 'S':
            for item in todos:
                print(item)
        case 'Q':
            break
        case 'E':
            serial_number = int(input("\n\nEnter the item number to edit: ")) - 1
            if len(todos) > serial_number > -1:
                current_todo = todos[serial_number]
                new_todo = input(f"\nEdit todo ({current_todo}): ")
                todos[serial_number] = new_todo
            else:
                print("\nWe can't find the item")

        case _:
            print("\nInvalid option. Application will quit now!!")
            break

print("See ya!")
