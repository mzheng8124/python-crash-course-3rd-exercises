# assign variables
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

# testing print messages
print(f"Hello {full_name.title()} !")
print(f"Hello {first_name.lower()} {last_name.upper()}")

# assigning variable a full message
message = (f"Hello {full_name.title()}")
print(message)

# notes: use \t for tab \n for newline
# ex print("\tPython")
# ex print("Languages:\nPython\nC\nJavaScript")
# strip() can be used to get rid of whitespace
# can also use lstrip() and rstrip()

# testing .removeprefix()
url = "https://youtube.com"
print(url.removeprefix("https://"))

# assigning the new value after .removeprefix
url = url.removeprefix("https://")
print(url)