# example of a function accepting as many arguments as need
# known as arbitary arguments
# uses '*' to start, must be placed last in parameter

# create function
def make_pizza(*toppings):
    # summarize pizza being created
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')

# call function
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')