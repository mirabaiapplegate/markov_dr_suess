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

    green_all_words = text_string.split(' ') # splitting string by space in text_string assiged as geen_all_words
    for i in range(len(green_all_words)-2):  # created for loop to get the range and leangth of green_all_words 
        current_key = (green_all_words[i], green_all_words[i+1])
        current_value = green_all_words[i+2]

        # print "CURRENT KEY: " + str(current_key)
        if current_key in chains:
            # print"found"
            # print "current:" + str(chains[current_key])
            chains[current_key].append(current_value)
        else:
            # print "not in here"
            chains[current_key] = [current_value]
    print chains

    return chains

chains = make_chains(input_text)

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     text = ""

#     # your code goes here

#     return text


# input_path = "green-eggs.txt"

# Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
