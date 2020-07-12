'''
Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

Note: If a character is repeated, treat each occurence as distinct,
for example an input of 'xxx' would return a list with 6 "versions" of 'xxx'
'''
def permute(s):

    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:

        # For every letter in string
        for i, let in enumerate(s):

            #For every permutation resulting from previous steps
            for perm in permute(s[:i] + s[i + 1:]):

                # Add to the output
                out += [let+perm]

    return out