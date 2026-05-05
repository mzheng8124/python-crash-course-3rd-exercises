# example using a slice
# notes
# works similar to range(), will stop one number before second delcared number
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])

# using the slice in a for loop
print('Here are the first three players:')

# using for loop
for player in players[:3]:
    print(player.title())
