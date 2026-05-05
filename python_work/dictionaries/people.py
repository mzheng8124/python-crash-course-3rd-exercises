# Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

# create dictionaries
person1 = {   
    'first_name' :'sarah',
    'last_name' : 'may',
    'age' : 18
}

person2 = {
    'first_name' :'devin',
    'last_name' : 'may',
    'age' : 18
}
person3 = {
    'first_name' :'kevin',
    'last_name' : 'may',
    'age' : 18
}

# create list to store dictionaries
people = [person1, person2, person3]

# for loop to output
for person in people:
    print(person)

