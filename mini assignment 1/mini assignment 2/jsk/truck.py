from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(cls, jk_color, jk_doors, jk_gas_powered, jk_seats, jk_trunk_space):
        super().__init__(jk_color, jk_doors, jk_gas_powered)
        cls.jk_seats = jk_seats
        cls.jk_trunk_space = jk_trunk_space

    def is_valid_number(cls, value):
        return isinstance(value, int) and value > 0

    @property
    def jk_seats(cls):
        return cls.__jk_seats

    @jk_seats.setter
    def jk_seats(cls, value):
        if cls.is_valid_number(value):
            cls.__jk_seats = value
        else:
            raise ValueError("Seats must be a positive integer")

    @property
    def jk_trunk_space(cls):
        return cls.__jk_trunk_space

    @jk_trunk_space.setter
    def jk_trunk_space(cls, value):
        if cls.is_valid_number(value):
            cls.__jk_trunk_space = value
        else:
            raise ValueError("Trunk space must be a positive integer")

    def __str__(cls):
        return f"{super().__str()}, Seats: {cls.jk_seats}, Trunk Space: {cls.jk_trunk_space}"

    def is_eco_friendly(cls):
        return super().is_eco_friendly() and (cls.jk_seats <= 2 and cls.jk_trunk_space == 0)
