# 9-1. Restaurant: Make a class called Restaurant. The __init__() 
# method for Restaurant should store two attributes: a restaurant_name
# and a cuisine_type. Make a method called describe_restaurant() that
# prints these two pieces of information, and a method called 
# open_restaurant() that prints a message indicating that the restaurant 
# is open. Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call describe_restaurant() for
# each instance.

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


# create instance
my_restaurant = Restaurant("Big Cooks", "American")
parent_restaurant = Restaurant("Small Cooks", "Chinese")
your_restaurant = Restaurant("Medieum Cooks", "Mexican")

# call method
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

parent_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
    
