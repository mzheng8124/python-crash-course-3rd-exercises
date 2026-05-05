# Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your
# list and as you do, print everything you know about each pet.

pet1 = {
    'pet' : 'cat',
    'owner_first_name' : 'susie',
    'owner_last_name' : 'may'
}

pet2 = {
    'pet' : 'dog',
    'owner_first_name' : 'sarah',
    'owner_last_name' : 'may'
}

pet3 = {
    'pet' : 'bird',
    'owner_first_name' : 'devin',
    'owner_last_name' : 'may'
}

pet4 = {
    'pet' : 'lizard',
    'owner_first_name' : 'kevin',
    'owner_last_name' : 'may'
}

# create list
pets = [pet1, pet2, pet3, pet4]

# for loop to iterate through list of dictionaries
for pet in pets:
    print(pet)