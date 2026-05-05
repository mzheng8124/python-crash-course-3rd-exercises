# example using function that can accept as 
# many key-value pairs as needed

# create function
def build_profile(first, last, **user_info):
    # dictionary containing everything we know about the user
    user_info['first_name'] = first
    user_info['last_name'] = last

    # return dictionary
    return user_info

# call function
user_profile = build_profile('devin', 'may', location = 'princeton', field = 'physics')

# output statement
print(user_profile)