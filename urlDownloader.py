'''
Poyo;       - 
Silver;     - we are going to have to make it get the file that contains all the urls from github if that's how you want it to find the urls

TODO: 
    - Requests --
    - Formatting -DONE-
    - Output must be a .txt file -DONE-
'''

from urllib.request import urlopen

list = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')

print("response", list) #actually just see what it's giving us, incase of errors



def update_list(current_diectory, next_directory):
    first_words = get_url()
    return first_words

def to_list(lines):
    new = []
    for line in lines:
        new.append(line)
    return new

# Get first word of each line
def get_url(lines):
    # for line in lines:
    #     print(line)
    return [str(line.split()[0])[2:-1] for line in lines]

digits = "0123456789."

# this one should work correctly Identation error
def get_ip(lines):
    new_lines = []
    for line in lines: #if not digits,then check if protoweb
        # check for each letter in line and see if it's not digits
        add_line = True
        for letter in line: # checking each letter in the line seeing if it's inside digits
            if not digits.contains(letter):
                add_line = False
        if add_line:
            new_lines.append(line) 
    return new_lines

"""I'm an octopus! =;O;="""
# lol



def get_info():
    with open(r'urls.txt', 'w+') as fn:
        url_llist = urlopen('https://raw.githubusercontent.com/ucanet/ucanet-registry/main/ucanet-registry.txt')
        for entry in to_list(url_llist):
            entry_parts = str(entry)[2:-3].split(" ")
            print(entry_parts)
            if entry_parts[2] == "protoweb":
                #Protoweb
                fn.write(f"p {str(entry_parts[0])} {str(entry_parts[2]).strip()}\n") 
            elif not entry_parts[2].__contains__("."):
                #Neocities
                fn.write(f"n {str(entry_parts[0])} {str(entry_parts[2]).strip()}\n") 
            else:
                #Raw IP - lets see if it works
                if str(entry_parts[2]).strip() != "0.0.0.0":
                    fn.write(f"i {str(entry_parts[0])} {str(entry_parts[2]).strip()}\n") 

get_info()