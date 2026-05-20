# example class representing a car
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
        # reject change if user tries to rollback and odometer
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll baack an odometer!")

    # method to increment the value of odometer
    def increment_odometer(self, miles):
        self.odometer_reading += miles

# create object
my_new_car = Car("audi", 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# changing the value by modifying it directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# call method to update value
my_new_car.update_odometer(52)
my_new_car.read_odometer()