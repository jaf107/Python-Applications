import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def find_meaning(w):
    w = w.lower()
    if w in data:
        meaning = data[w]
        return meaning
    elif len(get_close_matches(w, data.keys())) > 0:
        closest_word = get_close_matches(w,data.keys())[0]
        prompt = input("Did you mean %s instead? Enter Y if yes, or N if no." % closest_word)
        if prompt.lower() == 'y':
            return find_meaning(closest_word)
        elif prompt.lower() == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your reply."
    else:
        return "The word doesn't exist. Please double check it."


word = input('Enter word: ')

meaning = find_meaning(word)

if type(meaning) == list:
    for item in meaning:
        print(item)
        