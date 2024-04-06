
'''

Poyo;       - 
Silver;     - we are going to have to make it get the file that contains all the urls from github if that's how you want it to find the urls



TODO: 
    - Requuests
    - Formatting
    - Output must be a .txt file
'''

from urllib.request import urlopen

response = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')

print("response", response) #actually just see what it's giving us, incase of errors



def update_list(current_diectory, next_directory):
    first_words = get_first_word()
    return first_words




# Get first word of each line
def get_first_word(lines):
    # for line in lines:
    #     print(line)
    return [line.split()[0] for line in lines]


# Execute the function
first_words = get_first_word(response)

# Output
for word in first_words:
    print(str(word)[2:-1])
