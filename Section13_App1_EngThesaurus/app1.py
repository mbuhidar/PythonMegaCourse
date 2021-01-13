# Section 13 - App 1 - English Thesaurus

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):

    w = word.lower()
    
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? (y or n): ")
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
