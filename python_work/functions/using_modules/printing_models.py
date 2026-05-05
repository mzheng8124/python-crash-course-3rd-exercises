# 8-15. Printing Models: Put the functions for the example 
# printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify 
# the file to use the imported functions.

# import 
import printing_functions as pf

# create lists
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# call function 
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)




