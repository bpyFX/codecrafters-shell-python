import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    # Wait for user input
    user_input = input()

    #loop
    if user_input == "exit 0":
        sys.exit(0)
    elif user_input.startswith("echo "):
            print(user_input[5:])
    else:
        print(f"{user_input}: command not found")
    main()

if __name__ == "__main__":
    main()
