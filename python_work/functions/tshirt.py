# 8-3. T-Shirt: Write a function called make_shirt() 
# that accepts a size and the text of a message that should
# be printed on the shirt. The function should print a sentence 
# summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments.

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are
# large by default with a message that reads I love Python. Make a large
# shirt and a medium shirt with the default message, and a shirt of any 
# size with a different message.

# declare function
# use defualt values
def make_shirt(shirt_size="large", shirt_text="I love Python"):
    print(f"Shirt size is: {shirt_size.title()}, with printed message: {shirt_text}")

# call function 
# postional arguments
make_shirt("small", "HELLO!")

# keyword arguments
make_shirt(shirt_size="large", shirt_text="GOODBYE!")

# make large shirt with default message
make_shirt()

# make medium shirt with defualt message
make_shirt("medium")

# shirt any size with a different message
make_shirt("small", "Crazy different message!")