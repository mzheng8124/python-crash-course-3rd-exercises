# example using function that can accept as 
# many key-value pairs as needed

# step 2
# 8-13. User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.

# create function
def build_profile(first, last, **user_info):
    # dictionary containing everything we know about the user
    user_info['first_name'] = first
    user_info['last_name'] = last

    # return dictionary
    return user_info

# call function
user_profile = build_profile('devin', 'may', location = 'princeton', field = 'physics')
user_profile2 = build_profile('may', 'devin', location = 'na', field = 'na', sport = 'na')

# output statement
print(user_profile)
print(user_profile2)