# Think of things you could store in a list. For
# example, you could make a list of mountains, rivers, countries, cities,
# languages, or anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this
# chapter at least once.

# create list
things = ['mountains', 'rivers', 'countries', 'cities', 'languages']

# print list
print(things)


# append
things.append('cups')
print(things)

# pop
popped_thing = things.pop()
print(f'{popped_thing}, was removed from the list')
print(things)

# del
del things[4]
print(things)

# sort
things.sort()
print(things)

# sorted
print(sorted(things, reverse=True))
print(things)

# remove
things.remove('cities')
print(things)
