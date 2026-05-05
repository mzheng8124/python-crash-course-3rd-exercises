# 8-15. Printing Models: Put the functions for the example 
# printing_models.py in a separate file called printing_functions.py.
# Write an import statement at the top of printing_models.py, and modify 
# the file to use the imported functions.



# example using functions for list

# create function
def print_models(unprinted_designs, completed_models):
    # simulating printing each design until no designs are left
    # create loop
    while unprinted_designs:
        # create variable to store design
        current_design = unprinted_designs.pop()
        # output what design is being printed
        print(f"Printing model: {current_design}")
        # add design to completed list
        completed_models.append(current_design)

# create function to show completed models
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    # iterate through list
    for model in completed_models:
        print(model)

# create lists
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# call functions
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)