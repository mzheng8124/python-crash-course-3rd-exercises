# You just found out that your new dinner table
# won’t arrive in time for the dinner, and now you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names
# remain in your list. Each time you pop a name from your list, print a
# message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of
# your program.

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
guests.append('andrew')

# print new invite messages
print(f'{guests[0].title()}, please come to dinner.')
print(f'{guests[1].title()}, please come to dinner.')
print(f'{guests[2].title()}, please come to dinner.')
print(f'{guests[3].title()}, please come to dinner.')
print(f'{guests[4].title()}, please come to dinner.')

# new message
print('Whoops! Looks like only two people can come.')

# message to uninvited guests
first_pop = guests.pop()
print(f'Sorry {first_pop.title()}, you can not come to dinner anymore.')

second_pop = guests.pop()
print(f'Sorry, {second_pop.title()}, you can not come to dinner anymore.')

third_pop = guests.pop()
print(f'Sorry {third_pop.title()}, you can not come to dinner anymore.')

fourth_pop = guests.pop()
print(f'Sorry {fourth_pop.title()}, you can not come to dinner anymore.')

# print message to people still on list
print(f'{guests[0].title()}, you are still invited to come to dinner.')
print(f'{guests[1].title()}, you are still invited to come to dinner.')

# use del to remove last two people from list
del guests[0]

# guest is 0 bc list shifts left after first del is called
del guests[0]

# print list to check if it is empty
print(guests)
