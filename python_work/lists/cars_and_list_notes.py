# notes:
# using sort changes the order permanently
# sorting a cars list
# sorted() can be used to change the order temporarily ex: sorted(cars)
# sorted(reverse = True) can also be used to temorarily reverse the order
# reverse() can reverse the order of the list
# length() can be used to find the length of a list

# create lists that stores cars
cars = ['bmw', 'audi', 'toyota', 'subaru'] 

# use sorted() for temporary change
print('This is the temporary sorted list: ')
print(sorted(cars))

# orginal list
print('\nThis is the original list: ')
print(cars)

# use sort() to change list to alphabetical order
cars.sort()

# output list
print(cars)

# reverse alphabetical order using reverse = True
cars.sort(reverse=True)

# output list
print(f'\n{cars}')

# using reverse()
cars.reverse()
print(cars)

# using len
length = len(cars)
print(length)


