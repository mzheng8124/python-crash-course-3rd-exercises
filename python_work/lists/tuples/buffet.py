# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the change.
# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

# create tuple with five simple foods
foods = ('chicken', 'rice', 'salad', 'fruit', 'mac n cheese')

# use for loop to output values
for food in foods:
    print(food)

# trying to change value to receive error
# tried: foods[0] = 'beef' received error as aspected

# new tuple with two new items
foods = ('chicken', 'rice', 'salad', 'beef', 'noodle')

# use for loop to print new tuple
for food in foods:
    print(food)
