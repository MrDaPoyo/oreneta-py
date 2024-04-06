
'''

Silver;     - So now we need to go through each one and get the information about it right?
Poyo;       - Yeah

'''

lines = [""]

# Get first word of each line
def get_first_word(lines):
    return [line.split()[0] for line in lines]

# Execute the function
first_words = get_first_word(lines)

# Output
for word in first_words:
    print(word)