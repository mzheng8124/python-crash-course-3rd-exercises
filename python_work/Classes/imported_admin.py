# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly

from admin import User
from admin import Privileges
from admin import Admin

my_admin = Admin('Devin', 'May', 'Black', 'White')

my_admin.privileges.show_privileges()