import sys
import os

def validate_args(args, expect_length):
    if len(args) != expect_length:
        print(f'Error: {expect_length} arguments are required.')
        sys.exit(1)  # プログラムを終了する

def reverse(inputpath, outputpath):
    if os.path.exists(outputpath):
        print(f"Warning: The file '{outputpath}' already exists.")
        choice = input("Do you want to overwrite it? (yes/no): ").strip().lower()

        if choice == 'no':
            outputpath = input("Please enter a new output file path: ").strip()
        elif choice != 'yes':
            print("Invalid choice. Exiting.")
            sys.exit(1)

    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents[::-1])

def copy(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)

def duplicate_contents(inputpath, n):
    with open(inputpath) as f:
        contents = f.read()
    duplicate_content = contents * n    
    with open(inputpath, 'a') as f:
        f.write(duplicate_content)

def replace_string(inputpath, old_string, new_string):
    try:
        with open(inputpath) as f:
            contents = f.read()
        new_contents = contents.replace(old_string, new_string)

        with open(inputpath, 'w') as f:
            f.write(new_contents)
    except FileNotFoundError:
        print(f"Error: The file '{inputpath}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{inputpath}'.")
    except OSError as e:
        print(f"Error: An unexpected I/O error occurred: {e}")

def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "reverse":
        validate_args(sys.argv, 4)
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        reverse(inputpath, outputpath)

    elif command == "copy":
        validate_args(sys.argv, 4)
        inputpath = sys.argv[2]
        outputpath = sys.argv[3]
        copy(inputpath, outputpath)

    elif command == "duplicate-contents":
        validate_args(sys.argv, 4)
        inputpath = sys.argv[2]
        n = int(sys.argv[3])
        duplicate_contents(inputpath, n)

    elif command == "replace-string":
        validate_args(sys.argv, 5)
        inputpath = sys.argv[2]
        old_string = sys.argv[3]
        new_string = sys.argv[4]
        replace_string(inputpath, old_string, new_string)

    else: 
        print(f"Error: Unknown command '{command}'")
        sys.exit(1)

if __name__ == "__main__":
    main()