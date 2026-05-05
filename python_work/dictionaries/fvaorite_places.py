#  Make a dictionary called favorite_places. Think of
# three names to use as keys in the dictionary, and store one to three favorite
# places for each person. To make this exercise a bit more interesting, ask
# some friends to name a few of their favorite places. Loop through the
# dictionary, and print each person’s name and their favorite places.

# create dictionary
# storing values as a list
favorite_places = {
    'susie' : ['caf', 'bed', 'movies'],
    'devin' : ['gym', 'outside', 'bed'],
    'john' : ['trees', 'woods', 'mountains']
}

# output message
# use for loop to iterate through dictionary
for name, locations in favorite_places.items():
    print(f"{name.title()}")

    # use for loop to iterate through values list
    for location in locations:
        print(f'- {location}\n')
    
        