# 8-7. Album: Write a function called make_album() that builds a dictionary 
# describing a music album. The function should take in an artist name and 
# analbum title, and it should return a dictionary containing these two pieces of 
# information. Use the function to make three dictionaries representing 
# different albums. Print each return value to show that the dictionaries are 
# storing the album information correctly. Use None to add an optional
# parameter to make_album() that allows you to store the number of songs 
# on an album. If the calling line includes a value for the number of 
# songs, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of songs on an album.

# step 2:

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a 
# while loop that allows users to enter an album’s artist and title. Once
# you have that information, call make_album() with the user’s input and
# print the dictionary that’s created. Be sure to include a quit value 
# in the while loop.

# create function
def make_album(artist_name, album_title, songs=None):
    # declare dictionary
    albums = {}
    # add values to dictionary
    albums['Artist'] = artist_name.title()
    albums['Album Name'] = album_title.title()

    # check if songs has value
    if songs != None:
        albums['Songs'] = songs

    # return dictionary
    return albums

# call function
album1 = make_album('devin', 'Cry')
album2 = make_album('may', 'happy')
album3 = make_album('mike', 'sad')

# call including songs
album4 = make_album('bizzy', 'loud', 5)

# output each
print(album1)
print(album2)
print(album3)
print(album4)

# create the loop
while True:
    print("Enter 'q' at anytime to exit")
    artist_name = input("Enter the artist's name: ")

    # conditonal to check if user wants to exit
    if artist_name == 'q':
        break

    album_title = input("Enter the name of the album: ")

    # conditonal to check if user wants to exit
    if album_title == 'q':
        break

    # create varaible to store return value
    new_album = make_album(artist_name, album_title)

    # output statement
    print(new_album)




