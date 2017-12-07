#-*- coding: utf8 -*-

import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

# show a random quote

def show_random_quote(my_list):
	random_numb = random.randint(0, len(my_list) - 1)
	quote = my_list[random_numb]
	return quote

def capitalize(character):
	for character in characters:
		character.capitalize()

def message(character, quote):
	capitalize(character)
	capitalize(quote)
	return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme")

while user_answer != "B":
	print (message(show_random_quote(characters), show_random_quote(quotes)))
	user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme")


