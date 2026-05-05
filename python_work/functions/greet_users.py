# example of passing a list to a function
def greet_users(names):
    # print a message to each user in the list
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# create list
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)