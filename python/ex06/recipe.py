# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 20:14:50 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 13:09:45 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
	"Sandwhich" : {
		"meal" : "lunch",
		"prep_time" : 10,
		"ingredients" : ["ham", "bread", "cheese", "tomatoes"]
	},
	"Cake" : {
		"meal" : "dessert",
		"prep_time" : 60,
		"ingredients" : ["flour", "sugar", "eggs"]
	},
	"Salad" : {
		"meal" : "lunch",
		"prep_time" : 15,
		"ingredients" : ["avocado", "arugula", "tomatoes", "spinach"]
	}
}

def print_recipes():
	for key in cookbook:
		print(key)
	print()

def print_info(recipes=""):
	meals = []
	if recipes == "":
		recipes = input("Please enter a recipe name to get its details:\n>> ")
	try:
		new = recipes.capitalize()
		print("The recipe for {0}".format(recipes))
		print("\tIngredients list: {0}".format(cookbook[new]["ingredients"]))
		print("\tTo be eaten for {0}".format(cookbook[new]["meal"]))
		print("\tTakes {0} minutes of cooking".format(cookbook[new]["prep_time"]), end="\n\n")
	except:
		print_info(input("Please enter a recipe name to get its details:\n>> "))

def delete_recipe(recipes=""):
	if recipes == "":
		recipes = input("Please enter a recipe name to delete it:\n>> ")
	try:
		new = recipes.capitalize()
		print("{0} recipe deleted".format(recipes))
		del(cookbook[new])
	except:
		delete_recipe(input("Please enter a recipe name to delete it:\n>> "))
	
def user_add_recipe():
	recipe = input("\nEnter a name:\n>> ").capitalize()
	ingre = []
	print("\nEnter ingredients")
	i = 0
	while True:
		ingredi = input()
		if ingredi != "":
			ingre.append([ingredi])
		else:
			break
	meal = input("Enter a meal type:\n>> ")
	prep = input("Enter a preparation time:\n>> ")
	while prep.isnumeric() == False:
		prep = input("Enter a preparation time:\n>> ")
	cookbook.update({str(recipe) : {"meal" : str(meal), "prep_time" : str(prep), "ingredients" : ingre}})
	print()

def select_option():
	option = input("Please select a option:\n>> ")
	while True:
		if str(option).isnumeric() == False:
			print("Wrong option!")
			print("List of available option:\n  1: Add a recipe\n  2: Delete a recipe\n  3: Print a recipe\n  4: Print the cookbook\n  5: Quit", end="\n\n")
			option = input("Please select a option:\n>> ")
		elif int(option) < 1 or int(option) > 5:
			print("Wrong option!")
			print("List of available option:\n  1: Add a recipe\n  2: Delete a recipe\n  3: Print a recipe\n  4: Print the cookbook\n  5: Quit", end="\n\n")
			option = input("Please select a option:\n>> ")
		else:
			break
	opt = int(option)
	if opt == 1:
		user_add_recipe()
		cookbook_init()
	elif opt == 2:
		recipe = input("Please enter a recipe name to delete it:\n>> ")
		delete_recipe(recipe)
		cookbook_init()
	elif opt == 3:
		recipe = input("Please enter a recipe name to get its details:\n>> ")
		print_info(str(recipe))
		cookbook_init()
	elif opt == 4:
		print_recipes()
		cookbook_init()
	elif opt == 5:
		print("Cookbook closed! Goodbye :)", end="\n\n")
		exit()

def cookbook_init():
	print("Welcome to Python cookbook!")
	print("List of available option:\n  1: Add a recipe\n  2: Delete a recipe\n  3: Print a recipe\n  4: Print the cookbook\n  5: Quit", end="\n\n")
	select_option()

if __name__=='__main__':
	cookbook_init()
