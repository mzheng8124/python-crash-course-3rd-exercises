# Favorite Numbers: Use a dictionary to store people’s favorite
# numbers. Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in
# your dictionary. Print each person’s name and their favorite number. For
# even more fun, poll a few friends and get some actual data for your
# program.

# modified for part 2:
# so each person can have more than one favorite number. Then print
# each person’s name along with their favorite numbers.


# create dictionary
favorite_numbers = {
    'biz' : [42, 7, 87],
    'mike' : [3, 13, 7],
    'kobe' : [7, 18, 22],
    'mary' : [5, 6, 7],
    'steph' : [13, 6, 8]
}

# for loop to iterate through dictionary
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers:")

    # for loop to iterate through values list
    for number in numbers:
        print(f'- {number}')

