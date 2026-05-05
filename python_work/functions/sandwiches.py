# 8-12. Sandwiches: Write a function that accepts a list of items a person 
# wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a 
# summary of the sandwich that’s being ordered. Call the function three 
# times, using a different number of arguments each time.

# delcare function
def add_toppings(*sandwich_toppings):
    # print summary of sandwich
    print('\nThe following toppings will be added to your sandwich:')
    # iterate through tupple
    for topping in sandwich_toppings:
        print(topping)


# call function
add_toppings('cheese')
add_toppings('cheese', 'ham')
add_toppings('cheese', 'ham', 'turkey')
