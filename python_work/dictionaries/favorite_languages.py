# dictionary storing similar information
# example of using a dictionary storing people's favorite languages

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    }

# search up someone's favorite language
language = favorite_languages['sarah'].title()

# output message
print(f"Sarah's favorite language is {language}.")

# example using the get method
get_language = favorite_languages.get('mike', 'No value assigned.')

print(get_language)

# using sorted method
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll!")

# looping through all the values in the dictionary without including the keys
print(f"\nThe following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

# using set() to return data with no repeated information
print(f'\nReturning the list again with no reapeated languages:')

for language in set(favorite_languages.values()):
    print(language.title())

# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already
# taken the poll, print a message thanking them for responding. If they have
# not yet taken the poll, print a message inviting them to take the poll.

# create list
need_poll = ['jen', 'mike', 'sarah', 'biz']

for name in need_poll:
    if name in favorite_languages.keys():
        print(f'Thank you {name.title()} for taking the poll')
    else:
        print(f'{name.title()} please find some time to answer the poll.') 