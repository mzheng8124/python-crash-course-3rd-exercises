# example looping through a dictionary
user_0 = { 
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi', 
    }

# for loop
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# looping through only the keys
for name in user_0.keys():
    print(name)

