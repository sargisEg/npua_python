
def read_file(filename):
    try:
        with open(filename, 'r') as input_file:
            file_content = input_file.read()
            print("content:")
            print(file_content)
            return True
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return False

def write_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
    else:
        print("Writing to the file was successful.")
    finally:
        print("File has been closed.")


while True:
    filename = input("Enter the name of the file you want to open: ")
    
    try:
        if not read_file(filename):
            continue
    except ValueError:
        print("Invalid filename. Please enter a valid filename.")
        continue

    option = input("Do you want to write to this file? (y/n): ").lower()
    
    if option == 'n':
        filename = input("Enter the new name")
    
    new_content = input("Enter the new content to write to the file: ")
    try:
        write_file(filename, new_content)
    except ValueError:
        print("Invalid filename. Please enter a valid filename.")
