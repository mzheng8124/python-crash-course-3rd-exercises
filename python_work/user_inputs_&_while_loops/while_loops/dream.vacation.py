# Write a program that polls users about their dream 
# vacation. Write a prompt similar to If you could 
# visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

# create dictionary to store input
vacations = {}

# create flag to control loop
flag = True

# create loop 
while flag:

    # prompt user for information
    name = input("Please enter your name: ")
    response = input('If you could visit one place in the entire world, where would you go? ')

    # store information inside dictionary
    vacations[name] = response

    # prompt user if more users are taking the quiz
    repeat = input("Are there more people trying to answer? (yes/no): ")

    # if conditional to check user input
    if repeat == "no":
        flag = False

# let user know poll is over
print("\n--- Results ---\n ")

# iterate through dictionary for responses
for name, response in vacations.items():
    print(f"{name.title()} would love to visit {response} someday!")




