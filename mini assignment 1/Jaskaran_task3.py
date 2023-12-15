class Color:  # Define class
    def __init__(self, color_name, hex_code):
        self.color_name = color_name
        self.hex_code = hex_code
    
    def __str__(self):
        return f"Color Name: {self.color_name}\nHex Code: {self.hex_code}"

my_color = Color("Blue", "#0000FF")  # Create object

print(f"Color Name: {my_color.color_name}")  # Output name
print(f"Hex Code: {my_color.hex_code}")  # Output code

print(str(my_color))  # Output summary
