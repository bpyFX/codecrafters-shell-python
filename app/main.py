import sys
import os
import subprocess

def main():
    # Get the current PATH environment variable set during execution
    path_dirs = os.getenv('PATH').split(os.pathsep)

    while True:
        # Prompt for user input
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()

        # Split the input into command and arguments
        parts = user_input.split()
        if not parts:
            continue

        command = parts[0]
        args = parts[1:]

        # Loop to handle different commands
        if user_input == "exit 0":
            sys.exit(0)
        elif command == "echo":
            print(" ".join(args))
        elif command == "type":
            if args:
                search_command = args[0]
                if search_command in {"echo", "type", "exit", "pwd"}:
                    print(f"{search_command} is a shell builtin")
                else:
                    found = False
                    for dir in path_dirs:
                        executable_path = os.path.join(dir, search_command)
                        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                            print(f"{search_command} is {executable_path}")
                            found = True
                            break
                    if not found:
                        print(f"{search_command}: not found")
            else:
                print("Usage: type <command>")
        elif command == "pwd":
            print(os.getcwd())
        else:
            found = False
            for dir in path_dirs:
                executable_path = os.path.join(dir, command)
                if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                    try:
                        result = subprocess.run([executable_path] + args, check=True)
                    except Exception as e:
                        print(f"Error executing {executable_path}: {e}")
                    found = True
                    break
            if not found:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
