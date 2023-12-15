class Color:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def __str__(self):
        return f"Name: {self.name}\nCode: {self.code}"

user_name = input("Enter a color name: ")
user_code = input("Enter a hex color code: ")

my_color = Color(user_name, user_code)

print(f"Name: {my_color.name}")
print(f"Code: {my_color.code}")

print(str(my_color))
