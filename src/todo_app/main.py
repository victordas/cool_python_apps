todos = []
try:
    file = open('src/todo_app/todos.txt', 'r')
    todos = file.readlines()
    file.close()
finally:
    print()


while True:
    user_action = input("Type A to add a new todo" \
    "\nType S to show current items in todos" \
    "\nType Q to quit the application" \
    "\nType E to edit a todo item" \
    "\nType R to remove a todo item" \
    "\n\nEnter an option: ").strip().upper()
    
    match user_action:
        case 'A':
            todo = input("\n\nEnter a todo: ") + "\n"
            todos.append(todo);
            file = open('src/todo_app/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'S':
            for index, item in enumerate(todos):
                print(f"{index + 1}: {item}")
            print("\n\n")
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
        case 'R':
            serial_number = int(input("\n\nEnter the item number to remove: ")) - 1
            if len(todos) > serial_number > -1:
                removed_todo = todos.pop(serial_number)
                print(f"\nRemoved todo: ({removed_todo})")
            else:
                print("\nWe can't find the item")
        case _:
            print("\nInvalid option. Retry!!")

print("See ya!")
