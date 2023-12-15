filename = input("Please enter a filename: ")

try:
    with open(filename, 'r') as file:
        file_contents = file.read()
        print(f"Contents of {filename}:\n{file_contents}")
except FileNotFoundError:
    print(f"The file {filename} was not found.")
except Exception as e:
    print(f"Error: {str(e)}")
