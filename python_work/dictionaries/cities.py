# Make a dictionary called cities. Use the names of three cities
# as keys in your dictionary. Create a dictionary of information about each city
# and include the country that the city is in, its approximate population, and
# one fact about that city. The keys for each city’s dictionary should be
# something like country, population, and fact. Print the name of each city and
# all of the information you have stored about it.

# create dictionary
cities = {
    'atlanta' : {
        'country' : 'america',
        'population' : 100,
        'fact' : 'dangerous'
    },

    'birmingham' : {
        'country' : 'america',
        'population' : 200,
        'fact' : 'dangerous'
    },

    'montgonmery' : {
        'country' : 'america',
        'population' : 300,
        'fact' : 'captial'
    }
}

# for loop to iterate through dictionary
for city, facts in cities.items():
    print(f'{city.title()}:')

    # iterate through values
    for topic, fact in facts.items():
        print(f'\t{topic}:')
        print(f'\t - {fact}')

    print()
    