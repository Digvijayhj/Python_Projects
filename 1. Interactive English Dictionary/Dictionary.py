#---------------------------------------------------------------------"

#     *------     Interactive English Dictionary    -------*          #

#---------------------------------------------------------------------"

import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())):
        yn = input("Did you mean %s instead? Enter Y is yes or N is no: " % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist! Please double check it."
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

result = translate(word)
if type(result) == list:
    for statement in result:
        print(statement)
else:
    print(result)