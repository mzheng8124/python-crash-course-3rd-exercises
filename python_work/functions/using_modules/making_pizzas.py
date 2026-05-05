# example of using import
# import a specific funcion
    # 'from pizza import make_pizza'
# can give function an alias as well
# example of alias 'from pizza import make_pizza as mp'
    # mp(16, 'pepperoni')
# we can give modules and alias as well 
    # import pizza as p
    # p.make_pizza(16, 'pepperoni')
# we can also import all functions
    # from pizza import *
    # this approach is not recommended
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'pepperoni', 'cheese')