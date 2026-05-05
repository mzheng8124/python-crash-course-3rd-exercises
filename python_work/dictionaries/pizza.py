# storing a list in a dictionary

# create dictionary
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

# print out the order
print(f'You ordered a {pizza['crust']}-crust pizza'
      'with the following toppings:')

for topping in pizza['toppings']:
    print(f'\t{topping}')
