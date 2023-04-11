# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 20:14:50 by preina-g          #+#    #+#              #
#    Updated: 2023/04/11 21:12:13 by preina-g         ###   ########.fr        #
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

def print_info(recipes=""):
	if recipes == "":
		return
	else:
		print(cookbook[recipes])

def delete_recipe(recipes=""):
	if recipes == "":
		return
	else:
		del(cookbook[recipes])

if __name__=='__main__':
	print_recipes()
