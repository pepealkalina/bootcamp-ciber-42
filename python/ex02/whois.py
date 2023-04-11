# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 13:34:09 by preina-g          #+#    #+#              #
#    Updated: 2023/04/11 18:08:24 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argc = len(sys.argv)

if argc == 1:
	print()
elif argc >= 3:
	print("Error: so many arguments")
else:
	argv = sys.argv[1]
	if argv.isnumeric() == 0:
		print("Error: the argument is not an integer")
	else:
		num = int(argv)
		if num == 0:
			print("Its Zero ;)")
		elif num % 2 == 0:
			print("Its even")
		elif num % 2 == 1:
			print("Its odd")
