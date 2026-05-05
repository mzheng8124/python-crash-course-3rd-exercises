# Rivers: Make a dictionary containing three major rivers and the
# country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

# dictionary of rivers
rivers = {
    'nile' : 'egypt',
    'mississippi' : 'america',
    'yantze' : 'asia'
}

# loop to print a sentence about each river
for river, location in rivers.items():
    print(f"\nThe {river.title()} runs through {location.title()}")

# loop to print only the name of the river
for name in rivers:
    print('\nThe rivers include:')
    print(name.title())

# loop to print only the country 
for country in rivers.values():
    print('\nThe countries include')
    print(country.title())