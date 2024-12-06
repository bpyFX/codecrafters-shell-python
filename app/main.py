import sys


def main():
    #Used for type commands that are builtin
    valid_commands = ["echo", "type", "exit"]

    while True:
        # Uncomment this block to pass the first stage
        sys.stdout.write("$ ")
        # Wait for user input
        user_input = input()

        #loop
        if user_input == "exit 0":
            sys.exit(0)
        elif user_input.startswith("echo "):
            print(user_input[5:])
        elif user_input.startswith("type "):
            command = user_input[5:]
            if command in valid_commands:
                print(f"{command} is a shell builtin")
            else:
                print(f"{user_input[5:]}: command not found")
        else:
            print(f"{user_input}: command not found")

if __name__ == "__main__":
    main()
