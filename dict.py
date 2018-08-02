import json

data = json.load(open("data.json"))

def translate_word(define_word):
    define_word = define_word.lower()
    if define_word in data:
        return data[define_word]
    else:
        return "Sorry, this word cannot be found. Please double check it."

word = input("Enter word to define: ")

print(translate_word(word))