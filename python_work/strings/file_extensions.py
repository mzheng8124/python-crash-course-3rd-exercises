#  Python has a removesuffix() method that works
# exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable
# called filename. Then use the removesuffix() method to display the filename
# without the file extension, like some file browsers do.

# declare variable name
filename = "python_notes.txt"

# remove suffix using removesuffix()
print(filename.removesuffix(".txt"))

# update variable
filename = filename.removesuffix(".txt")
print(filename)