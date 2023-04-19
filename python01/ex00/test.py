# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 19:44:20 by preina-g          #+#    #+#              #
#    Updated: 2023/04/16 11:44:35 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

hola = ['si']

recipe = Recipe("hola", 5, 30, hola,"si", "lunch")

print(recipe)