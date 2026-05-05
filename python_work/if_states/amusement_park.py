# using python's if-elif-else statements

# delcare age variable
age = 12

# create conditional checks
if age < 4:
    price = 0

elif age < 18:
    price = 25

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

print(f'Your submission cost is ${price}.')