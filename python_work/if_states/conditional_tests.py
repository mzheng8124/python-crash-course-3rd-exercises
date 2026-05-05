# Conditional Tests: Write a series of conditional tests. Print a
# statement describing each test and your prediction for the results of each
# test. Your code should look something like this:
# car = 'subaru' 
# print("Is car == 'subaru'? I predict True.") 
# print(car == 'subaru') 
# print("\nIs car == 'audi'? I predict False.") 
# print(car == 'audi')
# Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5
# tests evaluate to False.

# delcare variable
car = 'toyota'

# create conditionals
print('Is car == Toyota? I predict false')
print(car == 'Toyota')

print('Is car.title == Toyota? I predict true')
print(car.title() == 'Toyota')

print('is car == toyota or car == Toyota? I predict true')
print(car == 'toyota' or car == 'Toyota')

print('is car.upper() == toyota or car.Upper() == Toyota? I predict false')
print(car.upper() == 'toyota' or car.upper() == 'Toyota')

print('is car == toyota and car.upper() = toyota? I predict false')
print(car == 'toyota' and car.upper() == 'toyota')

print('is car.lower == toyota and car == toyota? I predict true')
print(car.lower() == 'toyota' and car == 'toyota')

print('is car == TOYOTA? I predict false')
print(car == 'TOYOTA')

print('Is car.upper() == TOYOTA? I predict true')
print(car.upper() == 'TOYOTA')

print('Is car.upper() == TOYOTA or car == toyota? I predict true.')
print(car.upper() == 'TOYOTA' or car == 'toyota')

print('Is car.title() == TOYOTA and car == toyota? I predict false.')
print(car.title() == 'TOYOTA' and car == 'toyota')

# test using a list
cars = ['toyota', 'honda', 'subaru', 'ford']

# checking to see if item is in the list
if 'toyota' in cars:
    print('We do have this car in the list!')

# check to see if an item is not in the list
if 'bmw' not in cars:
    print('We do not have this car in the list!')