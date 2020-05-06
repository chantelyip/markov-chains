"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents_file = open('green-eggs.txt')
    contents_string = contents_file.read().replace('\n',' ')

    contents_file.close()
    return contents_string 


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {} 
    i = 0

    words_list = text_string.split()  

    for i in range(len(words_list) - 2):  

        key = (words_list[i], words_list[i + 1]) 
        value = words_list[i + 2]  
    
        new_list = chains.get(key, [])
        new_list.append(value)

        chains[key] = new_list

    for key, value in chains.items():
        print (key, value)

    return chains
# print(make_chains(open_and_read_file('text_string')))

def make_text(chains):
    """
    Return text from chains. Use dictionary to pick a random tuple to start with and go down
    the row of picking 

    bigram_variable =

    """

    words = []
    return " ".join(words)


input_path = "green-eggs.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
