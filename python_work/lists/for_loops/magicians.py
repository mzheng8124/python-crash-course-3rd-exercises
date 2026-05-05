# notes:
# magician is a temporary variable in this case
# temporary variables should have meaninful names

# using a for loop

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician)
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print final message
print('Thank you, everyone. That was a great magic show!')