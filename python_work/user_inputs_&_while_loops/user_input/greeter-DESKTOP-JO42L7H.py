# should use clear prompts when using input()
name = input('Please enter your name: ')
print(f'\nHello, {name}')

# using a prompt to build multiline strings
prompt = 'if you share your name, we can personalize' \
'the messages you see.'

prompt += '\nWhat is your first name? '

name = input(prompt)
print(f'\nHello, {name}!')