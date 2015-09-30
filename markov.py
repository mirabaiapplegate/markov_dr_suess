from random import choice


# opening file 
file_path = open("green-eggs.txt")


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # reading our file
    green_text = file_path.read()

    # returning text from file
    return green_text

# calling the above function and binding its' output to the variable input_text
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
    # creating an empty dictionary: chains
    chains = {}

    # replacing all new line characters with a empty space
    stripped_words = text_string.replace('\n', ' ')
    # replacing all the questionmarks with nothing.
    stripped_questionmark_words = stripped_words.replace('?', '')
    # stripping the empty space characters from the right and left side
    stripped_questionmark_words = stripped_questionmark_words.strip()
    # splitting the words by space
    green_all_words = stripped_questionmark_words.split(' ') 

    # looping through indexes of and ending the loop and the second to last index...so we don't have an 
    #incomplete tuple. (our tuples have to have 2 words)
    # (eggs, ham)
    for i in range(len(green_all_words)-2):  
        # current_key is our current tuple
        current_key = (green_all_words[i], green_all_words[i+1])  
        # current_value is each word that follows a current_key
        #ex: current_value = ('Would', 'you')
        #        current_value = ["could"] or ["like"]
        current_value = green_all_words[i+2]

        #looping through dictionary(chains) for current keys which are tuples
        if current_key in chains:  
            # if our tuple is already present, then append current_value ('could' or 'like') to chains
            chains[current_key].append(current_value) 
        # else if the current_key isn't in our dictionary, we put it there with and set current_value
        # as its initial item in list ('could')
        else:
            chains[current_key] = [current_value]
    #returns our dictionary named chains
    return chains
#calling this function and assigning its result to chains.
chains = make_chains(input_text)


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    # making a blank string
    text = ""
    # getting our random tuple(chosen_key)
    chosen_key = choice(chains.keys())
    # creating our string
    #ex: "mouse Would you," 
    text = chosen_key[0] + ' ' + chosen_key[1] + ' '
    
    # looping over our dictionary until until all our tuples are used in above text, then returns None
    # otherwise its infinite.
    while chains.get(chosen_key, None): 
        # generating list associated with tuple(chosen_key)
        options = chains[chosen_key]
        # generating our random word from the list(options)
        chosen_word = choice(options)
        # adding the chosen_word to our text
        text = text + ' ' + chosen_word
        # assigning new tuple(chosen_key) for next loop cycle
        chosen_key = (chosen_key[1], chosen_word)

    #returning our text
    return text

#calling our function, and assigning what it returns to random_text
random_text = make_text(chains)

#printing our markov chain!
print random_text
