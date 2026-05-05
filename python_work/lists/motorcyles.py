# example of using a list 
motorcycles = ['honda', 'yamaha', 'suzuki',]
print(motorcycles)

# change value
motorcycles[0] = 'ducati'
print(motorcycles)

# use append() to add elements to an end of a list
motorcycles.append('ducati')
print(motorcycles)

# use insert() to insert a value into the list
# shifts other values to the right
motorcycles.insert(0, 'honda')
print(motorcycles)

# use del to an item from the list using its index
del motorcycles[0]
print(motorcycles)

# use pop to remove an item from the end of a list
# after pop you can still use the value
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# remove methond by using value
motorcycles.remove('yamaha')
print(motorcycles)