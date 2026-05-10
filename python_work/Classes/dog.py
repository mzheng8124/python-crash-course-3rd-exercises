# example of creating a class called dog
class Dog:
    # sample model to create a dog
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        # simulate a dog sitting in response to a command
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        # simulate a dog rolling over
        print(f'{self.name} rolled over!')

# creating an instance
my_dog = Dog('Willie', 6)

# creating another instance
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"my dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
your_dog.roll_over()

