# 9-9. Battery Upgrade: Use the final version of electric_car.py from 
# this section. Add a method to the Battery class called 
# upgrade_battery(). This method should check the battery size and set the
# capacity to 65 if it isn’t already. Make an electric car with a default
# battery size, call get_range() once, and then call get_range() a second
# time after upgrading the battery. You should see an increase in the 
# car’s range.

# simple representation of a car

# create classs
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# example of creating another class to help represent battery
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge") 
    # add method to upgrade battery
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        else:
            print('The battery capacity is already at  the max of 65!')
        

# create new class to represent a specific electric vehicle
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    # if parent class had this method, child class can override by 
    # having same method name
    def fill_gas_tank(self):
        print("This car doesn't have a gas Tank!")


# create new instance
my_car = ElectricCar("MZ", "DM121", '2077')
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()