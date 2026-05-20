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

# 9-4. Number Served: Start with your program from Exercise 9-1 
# (page 162). Add an attribute called number_served with a default value
# of 0. Create an instance called restaurant from this class. Print the
# number of customers the restaurant has served, and then change this 
# value and print it again. Add a method called set_number_served() that 
# lets you set the number of customers that have been served. Call this 
# method with a new number and print the value again. Add a method called
# increment_number_served() that lets you increment the number of
# customers who’ve been served. Call this method with any number you 
# like that could represent how many customers were served in, say, a 
# day of business.

# create class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    # method that describes the two attributes provided
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.name}")
        print(f"They serve {self.type} cuisine.")
    
    # method that prints a message saying the place is open
    def open_restaurant(self):
        print(f"{self.name} is now open!")

    # method that sets the number of customers served
    def set_number_served(self, served):
        self.number_served = served
    
    # method that can increment the number of customers served
    def increment_number_served(self, increment):
        self.number_served += increment


# create instance
my_restaurant = Restaurant("Big Cooks", "American")
parent_restaurant = Restaurant("Small Cooks", "Chinese")
your_restaurant = Restaurant("Medium Cooks", "Mexican")

# call method
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

parent_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()

# create instance called restaurant
restaurant = Restaurant('Restaurant', 'Korean')
print(f'Restaurant has served {restaurant.number_served} customers')

# change value print again
restaurant.number_served = 13
print(f'Restaurant has served {restaurant.number_served} customers')

# set value using method
restaurant.set_number_served(50)
print(f'Restaurant has served {restaurant.number_served} customers')

# call method to increment value, then print new result
restaurant.increment_number_served(50)
print(f'Restaurant has served {restaurant.number_served} customers')
    
