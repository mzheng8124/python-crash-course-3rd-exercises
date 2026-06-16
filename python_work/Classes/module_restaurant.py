# storing restaurant class module here 

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