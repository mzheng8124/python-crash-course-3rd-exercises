# If you could invite anyone, living or deceased, to dinner,
# who would you invite? Make a list that includes at least three people you’d
# like to invite to dinner. Then use your list to print a message to each person,
# inviting them to dinner.

# create list
guests = ['bizzy', 'mary', 'kobe']

# variables to store guests
guest1 = guests[0]
guest2 = guests[1]
guest3 = guests[2]

# message to bizzy
placeholder = guest1
message = f'{placeholder}, please come to dinner.'
print(message)

# message to mary
placeholder = guest2
message = f'{placeholder}, please come to dinner.'
print(message)

# message to kobe
placeholder = guest3
message = f'{placeholder}, please come to dinner.'
print(message)

# same output using just the list 
print(f'{guests[0]}, please come to dinner')
print(f'{guests[1]}, please come to dinner')
print(f'{guests[2]}, please come to dinner')