# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 18:23:27 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 13:29:51 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata00.py file
kata = (19,42,21)

s = ', '.join(map(str, kata))
out = "The {} numbers are: {}"
print(out.format(len(kata), s))
