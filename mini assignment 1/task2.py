user_filename = input("Enter the name of the file you want to access: ")
try:
    with open(user_filename, 'r') as user_file:
        file_contents = user_file.read()
        print(f"File contents of {user_filename}:\n{file_contents}")
except FileNotFoundError:
    print(f"The specified file '{user_filename}' was not found.")
except Exception as ex:
    print(f"An error occurred: {str(ex)}")
