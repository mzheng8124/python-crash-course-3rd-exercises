# example using modulo %
number = input("Enter a number, and I'll tell you if " \
"it's even or odd: ")

# convert string to int
number = int(number)

# if conditional to check
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")