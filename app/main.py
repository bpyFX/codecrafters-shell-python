"""Minimal shell implementation used for the CodeCrafters challenge."""

import sys  # Provides access to stdin/stdout and exit routines
import os  # Interacts with the operating system (PATH, cwd, etc.)
import subprocess  # Used to run external commands

def builtin_pwd(_args: list[str]) -> None:
    """Handle the built-in `pwd` command by printing the cwd."""

    # `os.getcwd()` returns the current working directory which we simply output
    print(os.getcwd())

def execute_command(command: str, args: list[str], path_dirs: list[str]) -> None:
    """Execute a command by searching PATH and handling builtins."""

    # Handle the simple built-in `echo` command ourselves.
    if command == "echo":
        # Join all arguments with spaces and print them back to the user
        print(" ".join(args))

    # Implementation of the `type` builtin which tells the user whether a
    # command is built into the shell or where it exists on disk.
    elif command == "type" and args:
        if args[0] in {"echo", "type", "exit", "pwd", "cd"}:
            # Inform the user that the command is handled directly by the shell
            print(f"{args[0]} is a shell builtin")
        else:
            # Otherwise search through PATH directories for the executable
            for dir in path_dirs:
                executable_path = os.path.join(dir, args[0])
                if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                    print(f"{args[0]} is {executable_path}")
                    return
            # Reaching here means the command wasn't found anywhere
            print(f"{args[0]}: not found")

    # `pwd` is another builtin which simply prints the current directory
    elif command == "pwd":
        builtin_pwd(args)

    # Change directories for the `cd` builtin.
    elif command == "cd" and args:
        try:
            # Expand '~' to the user's home directory if present
            os.chdir(args[0].replace("~", os.getenv("HOME", "")))
        except FileNotFoundError:
            # Display the same error message format as real shells
            print(f"cd: {args[0]}: No such file or directory")

    # For all other commands we look for an executable in PATH
    else:
        for dir in path_dirs:
            executable_path = os.path.join(dir, command)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                try:
                    # Execute the program with provided arguments and wait for it to finish
                    subprocess.run([executable_path] + args, check=True)
                except Exception as e:
                    # Catch any exception and surface an error message
                    print(f"Error executing {executable_path}: {e}")
                return
        # Command not found anywhere on PATH
        print(f"{command}: command not found")

def main() -> None:
    """Entry point for the REPL loop."""

    # Pre-split the PATH environment variable for quick lookups later
    path_dirs = os.getenv("PATH").split(os.pathsep)

    # Run a read-eval-print loop until the user exits
    while True:
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read the user's input and ignore empty lines
        user_input = input().strip()
        if not user_input:
            continue

        # Separate the command from its arguments
        parts = user_input.split()
        command, args = parts[0], parts[1:]

        # Special case: exit when the user types `exit 0`
        if command == "exit" and args == ["0"]:
            sys.exit(0)

        # Delegate execution to the handler above
        execute_command(command, args, path_dirs)

if __name__ == "__main__":
    # Only run the REPL loop when executed directly (not when imported)
    main()
