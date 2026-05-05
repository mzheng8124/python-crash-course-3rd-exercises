# Deli: Make a list called sandwich_orders and fill it with the names of 
# various sandwiches. Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each 
# order, such as I made your tuna sandwich. As each sandwich is made,
# move it to the list of finished sandwiches. After all the sandwiches 
# have been made,print a message listing each sandwich that was made.

# create lists
sandwich_orders = ['ham','pastrami', 'turkey', 'pastrami', 'olive', 'tomato', 'pastrami', 'bacon']
finished_sandwiches = []

# message to let user know the deli has run out of pastrami
print("We are currently out of pastrami! Sorry for the inconviences.")

# while loop to remove pastrami 
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# create loop
# loop will run as long as this list is not empty
while sandwich_orders:

    # create variable to store values
    finished_sandwich = sandwich_orders.pop()

    # print message to user
    print(f"I have finished your {finished_sandwich} sandwich!")

    # add values to finished_sandwiches list
    finished_sandwiches.append(finished_sandwich)

# print statement saying each sandwich that was create
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich was made!")
