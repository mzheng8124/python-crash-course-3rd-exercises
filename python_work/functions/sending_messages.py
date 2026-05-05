# 8-10. Sending Messages: Start with a copy of your program from Exercise 
# 8-9. Write a function called send_messages() that prints each text 
# message and moves each message to a new list called sent_messages as 
# it’s printed. After calling the function, print both of your lists 
# to make sure the messages were moved correctly

# create function to show messages from a list
def show_messages(messages):
    # iterate through list
    for message in messages:
        print(message)

# create function to move each message to a new list
def send_messages(messages, sent_messages):
    # iterate through list
    while messages:
        # create variable to store removed value
        sent = messages.pop(0)
        # output removed value
        print(sent)
        # add value to list
        sent_messages.append(sent)


# create lists
messages = ['I love you!', 'I miss you!', 'I want to see you again soon!']
delivered_messages = []

# call function
show_messages(messages)
send_messages(messages, delivered_messages)

# output lists
print(messages)
print(delivered_messages)