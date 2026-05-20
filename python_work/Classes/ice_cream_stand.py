# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of 
# restaurant.Write a class called IceCreamStand that inherits from the 
# Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4
# (page 166). Either version of the class will work; just pick the one 
# you like better. Add an attribute called flavors that stores a list of 
# ice cream flavors. Write a method that displays these flavors. Create 
# an instance of IceCreamStand, and call this method.

# create class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    # method that describes the two attributes provided
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"They serve {self.type} cuisine.")
    
    # method that prints a message saying the place is open
    def open_restaurant(self):
        print(f"{self.name} is now open!")

# create IceCreamStand as a child class 
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['mango', 'strawberry', 'peach', 'cookies n cream']

    # method that displays ice cream flavors
    def display_flavors(self):
        print(f"The flavors of ice cream we have include: {self.flavors}")

    


# create instance
my_restaurant = Restaurant("Big Cooks", "American")
parent_restaurant = Restaurant("Small Cooks", "Chinese")
your_restaurant = Restaurant("Medieum Cooks", "Mexican")

# create an instance of IceCreamStand
my_icecream = IceCreamStand("BigIce", "Ice Cream")

# call method
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

parent_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()

# call method to return ice cream flavors
my_icecream.display_flavors()
    
