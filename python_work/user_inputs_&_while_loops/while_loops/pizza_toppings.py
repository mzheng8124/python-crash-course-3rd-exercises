# Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = 'Please enter the pizza topping you would like to add on your pizza.'
prompt += "\nEnter 'quit' to exit: "

# create loop
while True:
    message = input(prompt)

    # if conditional to check user choice
    if message == 'quit':
        break
    else:
        print(f'\n{message.title()} will be added to your pizza!\n')

