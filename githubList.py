
'''

Poyo;       - 
Silver;     - we are going to have to make it get the file that contains all the urls from github if that's how you want it to find the urls

got this code from a google search:


import urllib2  # the lib that handles the url stuff

data = urllib2.urlopen(target_url) # it's a file like object and works just like a file
for line in data: # files are iterable
    print line
oooo awesome!


TODO: 
    - Requuests
    - Formatting
    - Output must be a .txt file
'''

from urllib.request import urlopen

response = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')

def update_list(current_diectory, next_directory):
    first_words = get_first_word()
    return first_words

lines = [""]

# Get first word of each line
def get_first_word(lines):
    return [line.split()[0] for line in lines]

# Execute the function
first_words = get_first_word(lines)

# Output
for word in first_words:
    print(word)