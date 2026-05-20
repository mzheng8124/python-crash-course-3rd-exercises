# Users: Make a class called User. Create two attributes called 
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized
# greeting to the user. Create several instances representing different 
# users, and call both methods for each user.

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called 
# increment_login_attempts() that increments the value of login_attempts
# by 1. Write another method called reset_login_attempts() that resets 
# the value of login_attempts to 0. Make an instance of the User class 
# and call increment_login_attempts() several times. Print the value
# of login_attempts to make sure it was incremented properly, and then 
# call reset_login_attempts(). Print login_attempts again to make sure
# it was reset to 0.

# create class called user
class User:

    # create methods
    def __init__(self, first_name, last_name, hair_color, ethnicity):
        self.fname = first_name
        self.lname = last_name
        self.hcolor = hair_color
        self.ethnicity = ethnicity
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.fname} {self.lname} has {self.hcolor} hair and is {self.ethnicity} ")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}, I hope you are having a great day!")
    
    # method that increments login attempts by 1
    def increment_login_attempts(self):
        self.login_attempts += 1

    # method that resets login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
# create instances
my_user = User("Devin", "May", "black", "Indian")
your_user = User("May", "Devin", "red", "Irish")
other_user = User("Megan", "Xof", "black", "English" )

# call methods
my_user.describe_user()
my_user.greet_user()

your_user.describe_user()
your_user.greet_user()

other_user.describe_user()
other_user.greet_user()

# create new instance
test_user = User("test", "user", "black", "black")

# call methods 
print(f"{test_user.login_attempts}")
test_user.increment_login_attempts()
print(f"{test_user.login_attempts}")
test_user.increment_login_attempts()
print(f"{test_user.login_attempts}")
test_user.increment_login_attempts()
print(f"{test_user.login_attempts}")

# reset
test_user.reset_login_attempts()
print(f"{test_user.login_attempts}")
