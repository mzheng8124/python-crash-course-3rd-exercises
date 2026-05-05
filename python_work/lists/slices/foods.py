# copying a list using a slice
my_foods = ['pizza', 'falafel', 'carrot cake']

# new list that copies slice from my_foods
friend_food = my_foods[:]

# output to check lists
print("My list of foods are:")
print(my_foods)

print("\nMy friend's list of foods are:")
print(friend_food)

# try appending to each list
my_foods.append("apple")
friend_food.append("pear")

# print new lists
print(my_foods)
print(friend_food)

# 4-10. Slices: Using one of the programs you wrote in this chapter, add
# several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list

# print messages
print("The first three items in my_foods list are: ")
print(my_foods[0:3])

print("The two items in the middle of the list are: ")
print(my_foods[1:3])

print("The last three items in the list are: ")
print(my_foods[1:])

# for loop to print contents of my_foods list
for food in my_foods:
    print(food)

# for loop to print contents of friend_food list
for food in friend_food:
    print(food)



