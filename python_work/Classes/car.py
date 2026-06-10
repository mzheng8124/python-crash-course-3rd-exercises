# example class that can be used to represent a car
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # return a neatly formatted descriptive name
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # return odometer value
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # method to update value
    def update_odometer(self, mileage):
        # reject change if user tries to roll back odometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # method to increment the value of odometer
    def increment_odometer(self, miles):
        self.odometer_reading += miles


# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=40):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")

#     def get_range(self):
#         if self.battery_size == 40:
#             range_miles = 150
#         elif self.battery_size == 65:
#             range_miles = 225
#         else:
#             range_miles = 0

#         print(f"This car can go about {range_miles} miles on a full charge.")


# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()