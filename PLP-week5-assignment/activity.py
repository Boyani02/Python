# Base Class: Plane
class Plane:
    def __init__(self, model, speed):
        self.model = model  # Plane model
        self.speed = speed  # Speed in km/h

    def move(self):
        print(f"The {self.model} is flying at {self.speed} km/h.")

# Subclass 1: CommercialPlane
class CommercialPlane(Plane):
    def __init__(self, model, speed, capacity):
        super().__init__(model, speed)
        self.capacity = capacity  # Passenger capacity

    def move(self):
        print(f"The {self.model} is cruising at {self.speed} km/h, carrying {self.capacity} passengers.")

# Subclass 2: MilitaryPlane
class MilitaryPlane(Plane):
    def __init__(self, model, speed, weapon_system):
        super().__init__(model, speed)
        self.weapon_system = weapon_system  # Type of weapon system

    def move(self):
        print(f"The {self.model} is flying at {self.speed} km/h, ready for combat with {self.weapon_system}.")

# Subclass 3: CargoPlane
class CargoPlane(Plane):
    def __init__(self, model, speed, cargo_capacity):
        super().__init__(model, speed)
        self.cargo_capacity = cargo_capacity  # Cargo capacity in tons

    def move(self):
        print(f"The {self.model} is flying at {self.speed} km/h, carrying {self.cargo_capacity} tons of cargo.")

# Create instances of each plane type
commercial_plane = CommercialPlane("Boeing 737", 850, 150)
military_plane = MilitaryPlane("F-22 Raptor", 2410, "Air-to-Air Missiles")
cargo_plane = CargoPlane("C-130 Hercules", 650, 20)

# List of all planes
planes = [commercial_plane, military_plane, cargo_plane]

# Using polymorphism to call the move() method on each plane
for plane in planes:
    plane.move()  # Each plane will call its own version of move()
