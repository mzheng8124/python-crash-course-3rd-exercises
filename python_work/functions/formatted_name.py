# example using return values in functions

# delcare function
def get_formatted_name(first_name, last_name, middle_name=""):

    # if conditional if middle name is included
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

# call function
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name ('john', 'hooker', 'lee')
print(musician)