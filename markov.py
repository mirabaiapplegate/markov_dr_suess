from random import choice

file_path = open("green-eggs.txt")

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    green_text = file_path.read()

    return green_text

input_text = open_and_read_file(file_path)

def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    stripped_words = text_string.replace('\n', ' ')
    stripped_questionmark_words = stripped_words.replace('?', '')
    green_all_words = stripped_questionmark_words.split(' ') # splitting string by space in text_string assiged as geen_all_words
    

    for i in range(len(green_all_words)-2):  # created for loop to get the range and leangth of green_all_words 
        current_key = (green_all_words[i], green_all_words[i+1])  # tuples we assigned to var current keys when it iterates through loop add index of word 
        current_value = green_all_words[i+2]

        if current_key in chains:  #looping through dic chains for current keys which are tuples
            chains[current_key].append(current_value) # if current values are found in chains append vales to dic keys 
        else:
            chains[current_key] = [current_value]

    return chains

chains = make_chains(input_text)

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    chosen_key = choice(chains.keys())
    text = chosen_key[0] + ' ' + chosen_key[1] + ' '
    
    for i in range(30):  
        # generating our random word
        options = chains[chosen_key]
        chosen_word = choice(options)
        # word #2 from our tuple and new random word, combine them
         # creating our text that will print in the end
        text = text + ' ' + chosen_word
        chosen_key = (chosen_key[1], chosen_word)
        

    return text





random_text = make_text(chains)

print random_text
# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
