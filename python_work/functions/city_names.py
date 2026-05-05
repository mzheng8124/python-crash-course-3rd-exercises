# 8-6. City Names: Write a function called city_country() that takes in 
# the name of a city and its country. The function should return a string
# formatted like this "Santiago, Chile" Call your function with at least
# three city-country pairs, and print the values that are returned.

# declare function
def city_country(city, country):
    prompt = f'{city.title()}, {country.title()}'
    return prompt

# insert values
city1 = city_country('birmingham', 'america')
city2 = city_country('montgomery', 'america')
city3 = city_country('mechanicsville', 'america')

# output statements
print(city1)
print(city2)
print(city3)

