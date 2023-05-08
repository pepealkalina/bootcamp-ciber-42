# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 19:44:17 by preina-g          #+#    #+#              #
#    Updated: 2023/05/08 11:13:23 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	check_param(name, lvl, time, ingre, description, r_type):
    cheked = 1
    if not isinstance(name, str):
        print("Error: The name must be a string")
        cheked = 0
    else:
        try:
            if len(name) == 0:
                print("Error: There is no name.")
                cheked = 0
        except TypeError:
            pass
    if not isinstance(lvl, int):
        print("Error: The lvl must be a int")
        cheked = 0
    else:
        try:
            if lvl < 1 or lvl > 5:
                print("Error: The level mus be in a range from 1 to 5")
                cheked = 0
        except TypeError:
            pass
    if not isinstance(time, int):
        print("Error: The time must be a int")
        cheked = 0
    else:
        try:
            if time < 0:
                print("Error: The time must be positive")
                cheked = 0
        except TypeError:
            pass
    if not isinstance(ingre, list):
        print("Error: The Ingredients must be a list")
        cheked = 0
    else:
        try:
            if len(name) == 0:
                print("Error: There are no ingredients")
                cheked = 0
        except TypeError:
            pass
    if not isinstance(description, str):
        print("Error: The description must be a string")
        cheked = 0
    if not isinstance(r_type, str):
        print("Error: The recipe_type must be a string")
        cheked = 0
    else:
        try:
            if r_type != "starter" or r_type != "lunch":
                print("Error: The recipe type must be starter, lunch or dessert")
                cheked = 0
        except TypeError:
            pass
    return cheked

class Recipe:
    def __init__(self, name, lvl, time, ingre, description, r_type):
        
        if check_param(name, lvl, time, ingre, description, r_type) == 1:
            self.name = name
            self.cooking_lvl = lvl
            self.time = time
            self.ingredients = ingre
            self.description = description
            self.recipe_type = r_type
        else:
            exit()
        

    def __str__(self):
        txt = ""
        return txt