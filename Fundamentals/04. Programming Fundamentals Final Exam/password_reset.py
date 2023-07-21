password = input()

command = input()

while command != "Done":
    command_args = command.split()
    command_word = command_args[0]
    print_flag = True

    if command_word == "TakeOdd":
        password = [password[i] for i in range(len(password)) if i % 2 != 0]
        password = "".join(password)
    elif command_word == "Cut":
        index = int(command_args[1])
        lenght = int(command_args[2])

        substring = ""
        for i in range(index, index + lenght):
          substring += password[i]
        
        password = password.replace(substring, "", 1)
    elif command_word == "Substitute":
        substring = command_args[1]
        substitute = command_args[2]
        
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print_flag = False
            print("Nothing to replace!")
    if print_flag:   
        print(password)
    command = input()
print(f"Your password is: {password}")
