#-*- coding: utf8 -*-
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

user_answer = input("Tapez entrée pour découvrir une autre citation ou B pour quitter le programme")

if user_answer == "B":
    pass
elif user_answer == "C":
    print("C pas la bonne réponse")
else:
    #show another quote
	pass
def show_random_quote(my_list):
	# get a random number
	quote = my_list[0]
	return quote

print (show_random_quote(quotes))