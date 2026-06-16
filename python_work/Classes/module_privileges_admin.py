# module to store privileges and admin class from admin.py

# import user class
from module_user import User

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

