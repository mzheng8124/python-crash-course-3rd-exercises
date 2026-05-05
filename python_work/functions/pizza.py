# example of a function accepting as many arguments as need

# create function
def make_pizza(*toppings):
    # summarize pizza being created
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')

# call function
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')