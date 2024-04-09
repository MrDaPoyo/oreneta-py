'''
Poyo;       - okadoka
Silver;     - we are going to have to make it get the file that contains all the urls from github if that's how you want it to find the urls

TODO: 
    - Requests -DONE-
    - Formatting -DONE-
    - Output must be a .txt file -DONE-
    - Optimize code --
'''

from urllib.request import urlopen


def update_list(current_diectory, next_directory):
    first_words = get_info()
    return first_words

def to_list(lines):
    new = []
    for line in lines:
        new.append(line)
    return new

"""I'm an octopus! =;O;="""
# lol
"""Do you know where's my friend? """

def get_info():
    with open(r'urls.txt', 'w+') as fn:
        url_list = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')
        for entry in to_list(url_list):
            entry_parts = str(entry)[2:-3].split(" ")
            print(entry_parts)
            if entry_parts[2] == "protoweb":
                #Protoweb
                fn.write(f"p {str(entry_parts[0])} {str(entry_parts[2]).strip()},\n") 
            elif not entry_parts[2].__contains__("."):
                #Neocities
                fn.write(f"n {str(entry_parts[0])} {str(entry_parts[2]).strip()},\n") 
            else:
                #Raw IP
                if str(entry_parts[2]).strip() != "0.0.0.0":
                    fn.write(f"i {str(entry_parts[0])} {str(entry_parts[2]).strip()},\n") 
get_info()
