# Base Class: MilitaryPlane
class MilitaryPlane:
    def __init__(self, model, speed, range_, weapon_system):
        self.model = model  # The model of the plane
        self.speed = speed  # Speed in km/h
        self.range_ = range_  # Range in km
        self.weapon_system = weapon_system  # Type of weapon system on the plane

    def move(self):
        print(f"The {self.model} is flying at {self.speed} km/h with a range of {self.range_} km.")

    def attack(self):
        print(f"The {self.model} attacks with {self.weapon_system}.")

    def status(self):
        print(f"Plane Model: {self.model}")
        print(f"Speed: {self.speed} km/h")
        print(f"Range: {self.range_} km")
        print(f"Weapon System: {self.weapon_system}")


# Child Class: FighterJet (inherits from MilitaryPlane)
class FighterJet(MilitaryPlane):
    def __init__(self, model, speed, range_, weapon_system, stealth_ability):
        # Initialize attributes using the parent constructor
        super().__init__(model, speed, range_, weapon_system)
        self.stealth_ability = stealth_ability  # Stealth feature for the fighter jet

    def move(self):
        # Override the move method for FighterJet
        print(f"The {self.model} Fighter Jet is flying at supersonic speeds of {self.speed} km/h!")
        
    def status(self):
        # Display FighterJet-specific status information
        super().status()
        print(f"Stealth Ability: {self.stealth_ability}")


# Create objects (MilitaryPlanes and FighterJets)
plane1 = MilitaryPlane("Boeing 747", 900, 13000, "None")
fighter_jet1 = FighterJet("F-22 Raptor", 2410, 2300, "Air-to-Air Missiles", "Advanced Stealth")

# Displaying their functionalities
print("\nMilitary Plane 1 Status:")
plane1.status()
plane1.move()
plane1.attack()

print("\nFighter Jet 1 Status:")
fighter_jet1.status()
fighter_jet1.move()
fighter_jet1.attack()
