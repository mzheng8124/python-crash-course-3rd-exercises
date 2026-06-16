# module to store user class from admin.py
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