# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a 
# model name. It should then accept an arbitrary number of keyword 
# arguments. Call the function with the required information and two 
# other name-value pairs, such as a color or an optional feature. Your 
# function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information 
# was stored correctly.

# declare function
def car_info(manufacturer, model, **car_details):
    # link keys to values
    car_details['Manufacturer'] = manufacturer.title()
    car_details['Model'] = model.title()
    # return dictionary
    return car_details

# call function
car = car_info('subaru', 'outback', color = 'black', tow_package = True)

# output 
print(car)




