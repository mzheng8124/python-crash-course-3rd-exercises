# You just heard that one of your guests can’t
# make the dinner, so you need to send out a new set of invitations. You’ll
# have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of
# your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the
# name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in
# your list.

# create list
guests = ['bizzy', 'mary', 'kobe']

# remove one guest and output
popped_guest = guests.pop()
print(f'{popped_guest} will not be able to make it, invite someone else.')

# add one guest
guests.append('steph')

# create messages for each person in the list
print(f'{guests[0]}, please come to dinner.')
print(f'{guests[1]}, please come to dinner.')
print(f'{guests[2]}, please come to dinner.')