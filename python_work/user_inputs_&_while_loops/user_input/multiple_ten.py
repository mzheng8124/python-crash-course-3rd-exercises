# Ask the user for a number, and then report whether
# the number is a multiple of 10 or not.

# ask for user input
number = input("Enter a number and I'll check to see " \
"if the number is a multiple of 10: ")

# convert string to int
number = int(number)

# if conditional to check if 10 is a multiple
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")




