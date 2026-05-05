# 8-5. Cities: Write a function called describe_city() that accepts the
# name of a city and its country. The function should print a simple 
# sentence, such as Reykjavik is in Iceland. Give the parameter for the 
# country a default value. Call your function for three different cities,
# at least one of which is not in the default country.

# delcare function
def describe_city(city_name, country="america"):
    print(f"{city_name.title()} is in {country.title()}.")

# call function
describe_city("montgomery")
describe_city("birmingham")
describe_city('shanghai')