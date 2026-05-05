# 8-16. Imports: Using a program you wrote that has one function in it, 
# store that function in a separate file. Import the function into your 
# main program file, and call the function using each of these approaches:
# import module_name 
# from module_name import function_name
# from module_name import function_name as fn 
# import module_name as mn 
# from module_name import *

# import module_name
import pizza
pizza.make_pizza(16, 'pepperoni')

# from module_name import function_name
from pizza import make_pizza
make_pizza(12, 'cheese')

# from module_name import function_name as fn
from pizza import make_pizza as mp
mp(15, 'sausage')

# import module_name as mn 
import pizza as p
p.make_pizza(21, 'extra-cheese')

# from module_name import *
from pizza import *
make_pizza(24, 'bacon')


