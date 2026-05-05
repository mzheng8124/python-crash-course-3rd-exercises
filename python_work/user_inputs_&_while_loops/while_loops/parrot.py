# example of using while loop to end when user specifies
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 
 
active = True
while active:
    message = input(prompt)
    
    # if statement to check user prompt
    if message == 'quit':
        active = False
    else:
        print(message)