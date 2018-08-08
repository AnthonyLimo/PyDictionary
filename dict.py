import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))

def translate_word(define_word):
    define_word = define_word.lower()
    if define_word in data:
        return data[define_word]
    elif len(get_close_matches(define_word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes and N for no" % get_close_matches(define_word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(define_word, data.keys())[0]]
        elif yn == "N":
            return "We couldn't find your entry"
        else:
            return "The word doesn't exist in the entry"
    else:
        return "Sorry, this word cannot be found. Please double check it."

word = input("Enter word to define: ")

output = translate_word(word)

if type(output) == list:
    for item in output:
        print item
else:
    print(output)