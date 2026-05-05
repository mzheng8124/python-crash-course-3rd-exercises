# function example using positional arguments
def describe_pet(animal_type, pet_name):
    
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# call function
#describe_pet("hamster", 'harry')
#describe_pet("dog", "willie")

# using keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')


