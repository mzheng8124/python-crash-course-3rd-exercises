# example of returning a dictionary using a function call

# declcare function
# adding optional value age by using default value
def build_person(first_name, last_name, age=None):

    # create dictionary
    person = {'first': first_name, 'last': last_name}

    # check if age is given
    if age:
        person['age'] = age

    # return value
    return person

# create variable to store function return value
musician = build_person('jimi', 'hentrix')
print(musician)

musician = build_person('john', 'hentrix', '27')
print(musician)