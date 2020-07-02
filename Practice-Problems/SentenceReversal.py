'''
Given a string of words, reverse all the words. For Example:

Given:
    'This is the best'

Return:
    'Best the is This'

As a part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
    '    space here' and 'space here    '
both become:
    'here space'
'''
def rev_word(s):
    words = []
    length = len(s)
    space = [' ']

    i = 0

    while i < length:
        if s[i] not in space:
            word_start = i

            while i < length and s[i] not in space:
                i += 1
            
            words.append(s[word_start:i])

        i += 1

    return " ".join(reversed(words))