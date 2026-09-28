todos = []

while True:
    print("list, add, rm")
    command = input("command: ")
    if command == "list":
        print(todos)
    elif command == "add":
        val = input("what to add: ")
        if val not in todos:
            todos.append(val)
        else:
            print("already in list")
    elif command == "rm":
        val = input("what to remove: ")
        if val in todos:
            todos.remove(val)
        else:
            print("not in list")
    else:
        print("not a command")
    print("")
















    # try: 
    #     if command[0:4] == "list":
    #         print(todos)
    #     elif command[0:3] == "add":
    #         if command[3:] in todos:
    #             print("already in list")
    #         else: 
    #             todos.append(command[3:])
    #     elif command[0:2] == "rm":
    #         if command[2:] in todos:
    #             todos.remove[2:]
    #         else:
    #             print("does not exist")
    # except:
    #     print("something went wrong")