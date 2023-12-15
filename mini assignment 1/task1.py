file_name = input("Please enter a filename with an extension: ")

try:
    with open(file_name, 'a') as file:
        user_content = input("Please enter the content to append to the file: ")
        file.write(user_content)
        print(f"Content has been successfully appended to {file_name}.")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
