# Base Class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


# Subclass - Inheriting from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} takes off at {self.flight_speed} km/h and uses {self.power}!")


# Another Subclass
class TechSuperhero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} activates {self.gadget} to unleash {self.power}!")


# Example usage
hero1 = FlyingSuperhero("SkyRider", "Wind Control", "Cloud City", 300)
hero2 = TechSuperhero("CyberKnight", "Laser Blast", "Neo-Tokyo", "Arm Cannon")

hero1.display_info()
hero1.use_power()

print()

hero2.display_info()
hero2.use_power()
  