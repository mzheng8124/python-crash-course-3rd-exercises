# Write a program that asks the user how many
# people are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that their
# table is ready

# ask user for input
group = input('How many people are in your dinner group? ')

# string to int
group = int(group)

# if conditional to check number
if group > 8:
    print("Please wait a couple minutes for an available table.")
else:
    print("We have a table ready for you!")
