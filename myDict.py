import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	'''returns the word definition from dictionary'''

	if word in data:
		return data[word]
	elif word.lower() in data:
		return data[word.lower()]
	elif len(get_close_matches(word, data.keys())) > 0:
		suggestion = get_close_matches(word, data.keys())[0]
		confirmation = input("Did you mean %s instead? Y for yes, N for no" % suggestion)
		if confirmation == 'Y' or confirmation == 'y':
			print(suggestion)
			return(translate(suggestion))
		elif confirmation == 'n' or confirmation == 'N':
			return ("ok")
		else:
			return ("Command invalid")
	else:
		return("Word not found.")


while(True):
	word = input("Enter word: ")
	output = translate(word)

	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)


