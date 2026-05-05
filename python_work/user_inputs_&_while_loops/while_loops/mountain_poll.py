# create an empty dictionary
responses = {}

# create flag to control when loop ends
flag = True

# create loop
while flag:

    # prompt user for information
    name = input("\nWhat is your name? ")
    response = input("Which mountain whould you like to climb someday? ")

    # store responses inside the dictionary
    responses[name] = response

    # ask user if anyone esle is answering
    repeat = input("Is another person responding? (yes / no)")

    # if conditional to check user response
    if repeat == 'no':
        flag = False
    
# show results
print("\n--- Results --- ")

# use for loop to iterate through dictionary
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")


