# Use a variable to represent a person’s name, and
# include some whitespace characters at the beginning and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

# declare variable
name = "\n\t  Eric \t\n "
print(name)

# using lstrip()
print(name.lstrip())

# using rstrip()
print(name.rstrip())

# using strip()
print(name.strip())