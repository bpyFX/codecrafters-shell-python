import sys
import os
import subprocess

def execute_command(command, args, path_dirs):
    if command == "echo":
        print(" ".join(args))
    elif command == "type":
        if args:
            if args[0] in {"echo", "type", "exit", "pwd", "cd"}:
                print(f"{args[0]} is a shell builtin")
            else:
                for dir in path_dirs:
                    executable_path = os.path.join(dir, args[0])
                    if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                        print(f"{args[0]} is {executable_path}")
                        return
                print(f"{args[0]}: not found")
    elif command == "pwd":
        print(os.getcwd())
    elif command == "cd":
        if args:
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                print(f"cd: {args[0]}: No such file or directory")
        else:
            print("Usage: cd <directory>")
    else:
        for dir in path_dirs:
            executable_path = os.path.join(dir, command)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                try:
                    subprocess.run([executable_path] + args, check=True)
                except Exception as e:
                    print(f"Error executing {executable_path}: {e}")
                return
        print(f"{command}: command not found")

def main():
    path_dirs = os.getenv('PATH').split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = input().strip()
        if not user_input:
            continue

        parts = user_input.split()
        command, args = parts[0], parts[1:]

        if command == "exit" and args == ["0"]:
            sys.exit(0)

        execute_command(command, args, path_dirs)

if __name__ == "__main__":
    main()
