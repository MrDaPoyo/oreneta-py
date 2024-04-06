'''
Poyo;       - 
Silver;     - we are going to have to make it get the file that contains all the urls from github if that's how you want it to find the urls

TODO: 
    - Requuests
    - Formatting
    - Output must be a .txt file
'''

from urllib.request import urlopen
import json

list = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')

print("response", list) #actually just see what it's giving us, incase of errors



def update_list(current_diectory, next_directory):
    first_words = get_first_word()
    return first_words


# Get first word of each line
def get_first_word(lines):
    # for line in lines:
    #     print(line)
    return [str(line.split()[0])[2:-1] for line in lines]


# Execute the function
first_words = get_first_word(list)

# Output
for word in first_words:
    print(word)

"""I'm an octopus! =;O;="""
# lol

with open(r'urls.txt', 'w') as fp:
    for item in first_words:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')


# my code should work, and it just did work
"""My code also did and it's better swag Just kidding sorry don't get mad at me; Should we use both? kk"""
# it's fine lol