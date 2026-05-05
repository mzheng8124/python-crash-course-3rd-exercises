#  Checking Usernames: Do the following to create a program that
# simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of
# the new usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
# current_users containing the lowercase versions of all existing users.)

# create list of current users
current_users = ['mike', 'biz', 'kobe', 'mary', 'steph']

# create list of new users
new_users = ['mike', 'chloe', 'biz', 'amber', 'clest']

# copy of current_users in lower case
# using list comprehension
lower_case_current_users = [user.lower() for user in current_users]

# loop through new_users to check if name is already in current_users
for user in new_users:
    if user.lower() in lower_case_current_users:
        print(f'Hello {user}, this username has already been taken, please enter a new one.')
    else:
        print(f'Hello {user} this username is avaiable!')