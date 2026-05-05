# example using if statement in a list

# list using car brands
cars = ['audi', 'bmw', 'subaru', 'toyota'] 

# for loop to iterate through list
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())