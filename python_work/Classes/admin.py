# 9-7. Admin: An administrator is a special kind of user. Write a class
# called Admin that inherits from the User class you wrote in Exercise 9-3
# (page 162) or Exercise 9-5 (page 167). Add an attribute, privileges, 
# that stores a list of strings like "can add post", "can delete post", 
# "can ban user", and so on. Write a method called show_privileges() that
# lists the administrator’s set of privileges. Create an instance of 
# Admin, and call your method.

# 9-8. Privileges: Write a separate Privileges class. The class should
# have one attribute, privileges, that stores a list of strings as 
# described in Exercise 9-7. Move the show_privileges() method to this 
# class. Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its 
# privileges. 

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
# create privileges class
class Privileges:
    def __init__(self, privileges=["can add post", "can delete post", 'can delete user']):
        self.privileges = privileges

    # method that can show user privileges
    def show_privileges(self):
        print(f"Showing privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, hair_color, ethnicity):
        super().__init__(first_name, last_name, hair_color, ethnicity)
        self.privileges = Privileges()

# create instance
my_admin = Admin('Devin', 'May', 'black', 'white')

# call method
my_admin.privileges.show_privileges()


