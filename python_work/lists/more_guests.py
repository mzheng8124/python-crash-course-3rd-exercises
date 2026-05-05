# You just found a bigger dinner table, so now more space
# is available. Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
# end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

# create list
guests = ['bizzy', 'mary', 'kobe']

# remove one guest and output
popped_guest = guests.pop()
print(f'{popped_guest} will not be able to make it, invite someone else.')

# add one guest
guests.append('steph')

# use insert to add guests to beginning and middle
guests.insert(0, 'chloe')
guests.insert(2, 'celeste')

# use append to add one guest to the end of the list
guests.append('Andrew')

# print new invite messages
print(f'{guests[0].title()}, please come to dinner.')
print(f'{guests[1].title()}, please come to dinner.')
print(f'{guests[2].title()}, please come to dinner.')
print(f'{guests[3].title()}, please come to dinner.')
print(f'{guests[4].title()}, please come to dinner.')

# use len to show the number of guess
number = len(guests)
print(f'I am inviting {number} people to dinner.')







