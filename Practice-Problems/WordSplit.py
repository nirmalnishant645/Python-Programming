'''
Note, this is a more advanced problem than the previous two!
It aso has a lot of variation possibilities and we're ignoring strict requirements here.

Create a function called word_split() which takes in a string phrase and a set list_of_words.
The function will then determine if it is possible to split the string in a way in which words can be made from the list of words.
You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

For example:

INPUT: word_split('themanran',['the','ran','man'])
OUTPUT: ['the', 'man', 'ran']

INPUT:  word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])
OUTPUT: ['i', 'love', 'dogs', 'John']

INPUT:  word_split('themanran',['clown','ran','man'])
OUTPUT: []
'''

def word_split(phrase, words_list, output = None):

    if output is None:
        output = []

    for word in words_list:

        if phrase[:len(word)] == word:

            output.append(word)

            return word_split(phrase[len(word):], words_list, output)

    return output