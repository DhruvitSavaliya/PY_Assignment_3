#Write a Python program to show hybrid inheritance.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        return "Brand: ",self.brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car_details(self):
        return self.display_brand()," Model: ",self.model

class Bike(Vehicle):
    def __init__(self, brand, type_of_bike):
        super().__init__(brand)
        self.type_of_bike = type_of_bike

    def display_bike_details(self):
        return self.display_brand()," Type: ",self.type_of_bike

class ElectricBike(Car, Bike):
    def __init__(self, brand, model, type_of_bike, battery_capacity):
        Car.__init__(self, brand, model)  
        Bike.__init__(self, brand, type_of_bike)  
        self.battery_capacity = battery_capacity

    def display_details(self):
        return f"{self.display_brand()}, Model: {self.model}, Type: {self.type_of_bike}, Battery Capacity: {self.battery_capacity} kWh"

electric_bike = ElectricBike("Tesla", "Model X", "Electric Scooter", 15)

print(electric_bike.display_details())

