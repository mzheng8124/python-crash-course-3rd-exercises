# simple dictionary example using an alien
alien_0 = {'color' : 'green', 'points' : 5}

# print outputs
print(alien_0['color'])
print(alien_0['points'])

# if player shot down an alien
player_points = alien_0['points']

# print output
print(f'You have just earned {player_points} points!')

# adding new information to the dictionary
alien_0['x_postition'] = 0
alien_0['y_position'] = 25

# print output to see if new info has been added
print(alien_0)

# building a dictionary starting from an empty one
alien_1 = {}

# add key and value pairs
alien_1['color'] = 'green'
alien_1['points'] = 5

# output new dictionary
print(alien_1)

# change the value of key
# output original color
print(f'The alien is currently {alien_0["color"]}.')

# assign new value to the key 
alien_0['color'] = 'red'

# test change by printing
print(f'The alien is now {alien_0['color']}')

# example using an alien that can move
alien_move = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f'Original position {alien_move['x_position']}')

# alien moves to the right
# Determine how far to move the alien based on current speed
if alien_move['speed'] == 'slow':
    x_increment = 1
elif alien_move['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# update the old postion by adding the new postion to it
alien_move['x_position'] = alien_move['x_position'] + x_increment

# check output
print(f'New x position of the alien is {alien_move['x_position']}')


# using del to remove a value permanently
# print original 
print(alien_0)

# remove a key from dictionary
del alien_0['points']

# output to show removal
print(alien_0)