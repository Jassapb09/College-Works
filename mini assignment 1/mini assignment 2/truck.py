from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, num_doors, gas_powered, seats, trunk_space):
        super().__init__(color, num_doors, gas_powered)
        self.__seats = seats
        self.__trunk_space = trunk_space

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError("Seats must be a positive integer")

    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int) and value > 0:
            self.__trunk_space = value
        else:
            raise ValueError("Trunk space must be a positive integer")

    def __str__(self):
        return f"{super().__str()}, Seats: {self.__seats}, Trunk Space: {self.__trunk_space}"

    def is_eco_friendly(self):
        return super().is_eco_friendly() and (self.__seats <= 2 and self.__trunk_space == 0)
