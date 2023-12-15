
filename = input("Enter a filename with extension: ")

try:
    with open(filename, 'a') as file:

        content = input("Enter content to append to the file: ")
        
        file.write(content)
        print(f"Content appended to {filename} successfully.")
except FileNotFoundError:
    print(f"File {filename} not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
