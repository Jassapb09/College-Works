class Vehicle:
    def __init__(self, color, num_doors, gas_powered):
        self.__color = color
        self.__num_doors = num_doors
        self.__gas_powered = gas_powered

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if value in ['red', 'blue', 'green', 'black', 'white']:
            self.__color = value
        else:
            raise ValueError("Invalid color")

    @property
    def num_doors(self):
        return self.__num_doors

    @num_doors.setter
    def num_doors(self, value):
        if value in [2, 4, 5]:
            self.__num_doors = value
        else:
            raise ValueError("Invalid number of doors")

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise ValueError("Gas powered must be a boolean")

    def __str__(self):
        return f"Color: {self.__color}, Doors: {self.__num_doors}, Gas Powered: {self.__gas_powered}"

    def is_eco_friendly(self):
        return self.__num_doors == 2 and not self.__gas_powered