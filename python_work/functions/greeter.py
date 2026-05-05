# simple function that prints a greeting
#def greet_user(username):
    # display a simple greeting
    #print(f"Hello!, {username.title()}")

#greet_user('jesse')

# example using a while loop
def get_formatted_name(first_name, last_name): 
    # """Return a full name, neatly formatted.""" 
    full_name = f"{first_name} {last_name}" 
    return full_name.title() 

# This is an infinite loop!
# Add break conditionals 
while True:
    print("\nPlease tell me your name:") 
    print("Enter 'q' at anytime to quit")

    # prompt user for information
    f_name = input("First name: ") 
    if f_name == 'q':
        break
    l_name = input("Last name: ") 
    if l_name == 'q':
        break

    # output information
    formatted_name = get_formatted_name(f_name, l_name) 
    print(f"\nHello, {formatted_name}!")