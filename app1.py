import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    title = word.title()
    capital = word.upper()
    match = get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif title in data:
        return data[title]
    elif capital in data:
        return data[capital]
    elif len(match) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes , or N if no: " % match[0])
        if yn.lower() == 'y':
            return data[match[0]]
        elif yn.lower() == 'n':
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it"

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
