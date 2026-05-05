# A movie theater charges different ticket prices
# depending on a person’s age. If a person is under the age of 3, 
# the ticket is free; if they are between 3 and 12, the ticket is $10;
#  and if they are over age 12, the ticket is $15. Write a loop in 
# which you ask users their age, and then tell them the cost of their 
# movie ticket.

prompt = "Welcome to the Theater!\n Prices on tickets vary by age, please " \
"enter your age and I will inform you of how much your ticket costs."

prompt += "Enter 'quit' to exit: "
active = True

# create loop
while active:
    # create varaible to store and changed string to int value
    message = (input(prompt))

    # check if user wants to exit
    if message == 'quit':
        active = False
    else:
        # change message from string to int
        message = int(message)


    # if conditionals to determine price
    if message < 3:
        print('Your ticket is free')
    elif 3 <= message <= 12:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
