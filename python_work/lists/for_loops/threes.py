# Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list.

# using list comprehension
threes = [value + 3 for value in range(0,30,3)]
print(threes)

# using list()
numbers = list(range(3,33,3))
print(numbers)
