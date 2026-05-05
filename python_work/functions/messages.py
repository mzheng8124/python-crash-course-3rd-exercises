# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints each 
# text message.

# create function to show messages from a list
def show_messages(messages):
    # iterate through list
    for message in messages:
        print(message)

# create list 
messages = ['I love you!', 'I miss you!', 'I want to see you again soon!']

# call function
show_messages(messages)