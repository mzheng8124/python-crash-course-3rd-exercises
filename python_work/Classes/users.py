#  Users: Make a class called User. Create two attributes called 
# first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called 
# describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized
# greeting to the user. Create several instances representing different 
# users, and call both methods for each user.

# create class called user
class User:

    # create methods
    def __init__(self, first_name, last_name, hair_color, ethnicity):
        self.fname = first_name
        self.lname = last_name
        self.hcolor = hair_color
        self.ethnicity = ethnicity

    def describe_user(self):
        print(f"{self.fname} {self.lname} has {self.hcolor} hair and is {self.ethnicity} ")

    def greet_user(self):
        print(f"Hello {self.fname} {self.lname}, I hope you are having a great day!")
    
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
