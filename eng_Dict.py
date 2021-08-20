import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn= input("Did you mean %s? If yes enter 'Y' else enter 'N':" % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "Word not found!"
        else:
            return "Invalid entry!"
    else:
        return "Word not found!"

word=input("Enter Word:")
meaning=translate(word)

if type(meaning)==list:
    for item in meaning:
        print("Meaning: ",item,"\n")
else:
    print(meaning)
