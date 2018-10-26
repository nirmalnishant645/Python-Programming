import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if yn in ["Y", "y"]:
            return data[get_close_matches(word, data.keys())[0]]
        elif yn in ["N","n"]:
            return "The word doesn't exist!"
        return "Sorry, did not understand your entry."
    return "The word doesn't exist!"

word = input("Enter word: ").lower()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
