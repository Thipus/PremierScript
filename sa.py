#-*- coding: utf8 -*-
quotes = ["test1", "test2"]

import random
import json

def read_value_from_json(key, fichier):
	values = []
	with open(fichier) as f:
		data = json.load(f)
		for bob in data:
			values.append(bob[key])
		return values

# show a random quote

def show_random_quote(my_list):
	random_numb = random.randint(0, len(my_list) - 1)
	quote = my_list[random_numb]
	return quote

def random_character():
	all_values = read_value_from_json("character", "characters.json")
	return show_random_quote(all_values)

def random_quote():
	all_values = read_value_from_json("quote", "quotes.json")
	return show_random_quote(all_values)

def capitalize(character):
	for charac in character:
		charac.capitalize()

def message(character, quote):
	capitalize(character)
	capitalize(quote)
	return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme")

while user_answer != "b":
	print (message(random_character(), random_quote()))
	user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme")


