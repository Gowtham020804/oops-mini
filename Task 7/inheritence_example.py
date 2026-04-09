class Vehicle:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)


class Car(Vehicle):

    def car_type(self):
        print("This is a car")


class Bike(Vehicle):

    def bike_type(self):
        print("This is a bike")


# Objects
car1 = Car("Toyota", 180)
bike1 = Bike("Yamaha", 120)

print("Car Details")
car1.display_info()
car1.car_type()

print("\nBike Details")
bike1.display_info()
bike1.bike_type()