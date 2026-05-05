# consider how you
# might make a list of the first 10 square numbers (that is, the
# square of each integer from 1 through 10). In Python, two
# asterisks (**) represent exponents.

# create list
squares = []

# for loop
for value in range(1, 11): # value stops before last value so 1-10
    square = value ** 2
    squares.append(square)

# output list
print(squares)

# using min() and max()
minimum = min(squares)
maximum = max(squares)

# output values
print(f'The lowest value in the list is {minimum}.')
print(f'The highest value in the list is {maximum}.')

# using sum()
total = sum(squares)

# output
print(f'The values of all numbers added inside the list is {total}.')
