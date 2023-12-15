class Vehicle:
    jk_colors = ['red', 'blue', 'grey', 'black', 'white']
    jk_doors = [2, 4, 5]

    def __init__(self, jk_color, jk_doors, jk_gas_powered):
        if jk_color in Vehicle.jk_colors:
            self.jk_color = jk_color
        else:
            raise ValueError("Invalid color")

        if jk_doors in Vehicle.jk_doors:
            self.jk_doors = jk_doors
        else:
            raise ValueError("Invalid number of doors")

        if isinstance(jk_gas_powered, bool):
            self.jk_gas_powered = jk_gas_powered
        else:
            raise ValueError("Gas powered must be a boolean")

    def __str__(self):
        return f"Color: {self.jk_color}, Doors: {self.jk_doors}, Gas Powered: {self.jk_gas_powered}"

    def is_eco_friendly(self):
        return self.jk_doors == 2 and not self.jk_gas_powered
