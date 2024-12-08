import sys
import os
from sys import executable


def main():

    # Get the current PATH environment variable set during execution
    path_dirs = os.getenv('PATH').split(os.pathsep)

    #Used for type commands that are builtin
    valid_commands = ["echo", "type", "exit"]

    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        user_input = input()

        # Split the input into command and arguments
        parts = user_input.split()
        if not parts:
            continue


        command = parts[0]
        args = parts [1:]

        #loop
        if user_input == "exit 0":
            sys.exit(0)
        elif command == "echo":
            print(" ".join(args))
        elif command == "type":
            if args:
                search_command = args[0]
                if search_command in valid_commands:
                    print(f"{search_command} is a shell builtin")
                else:
                    found = False
                    for dir in path_dirs:
                        executable = os.path.join(dir, search_command)
                        if os.path.isfile(executable) and os.access(executable, os.X_OK):
                            print(f"{search_command} is {executable}")
                            found = True
                            break
                    if not found:
                        print(f"{search_command}: command not found")
            else:
                print("Usage: type <command>")
        else:
            found = False
            for dir in path_dirs:
                executable = os.path.join(dir, command)
                if os.path.isfile(executable) and os.access(executable, os.X_OK):
                    os.system(user_input)
                    found = True
                    break
            if not found:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
