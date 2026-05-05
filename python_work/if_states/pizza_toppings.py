# using multiple if statements

# delcare list of toppings
requested_toppings = ['mushrooms','green peppers', 'extra cheese']

# use if conditionals
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')

if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')

if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza!')

# use for loop
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers.')
    else:
        print(f'Adding {requested_topping}')

print('\nFinished making your pizza!')

# checking if the list is empty
# create an empty list
empty_list = []

# check for an empty list, returns true if the list has at least one item
# returns false if the list is empty
if empty_list:
    print('This is not an empty list.')

else:
    print('The list is empty.')

# create list to compare 
avaiable_toppings = ['mushrooms', "green peppers"]

# check to see if requested toppings are in avaiable toppings
# use a for loop to check
for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print(f"Adding {requested_topping} to your pizza.")
    else:
        print(f'Sorry we do not have {requested_topping}.')

# final output
print('\nFinished making your pizza!')
    