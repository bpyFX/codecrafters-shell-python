import sys
import os
import subprocess

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
        elif command == "echo":
            print(" ".join(args))
        elif command == "type":
            if args:
                if args[0] in {"echo", "type", "exit", "pwd"}:
                    print(f"{args[0]} is a shell builtin")
                else:
                    for dir in path_dirs:
                        executable_path = os.path.join(dir, args[0])
                        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                            print(f"{args[0]} is {executable_path}")
                            break
                    else:
                        print(f"{args[0]}: not found")
        elif command == "pwd":
            print(os.getcwd())
        else:
            for dir in path_dirs:
                executable_path = os.path.join(dir, command)
                if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                    try:
                        subprocess.run([executable_path] + args, check=True)
                    except Exception as e:
                        print(f"Error executing {executable_path}: {e}")
                    break
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()
