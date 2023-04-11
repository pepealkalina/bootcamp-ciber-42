# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:27:04 by preina-g          #+#    #+#              #
#    Updated: 2023/04/11 19:41:04 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
	print()
elif len(sys.argv) >= 4:
	print("To many arguments")
elif sys.argv[1].isnumeric() == False and sys.argv[2].isnumeric() == False:
	print("Error: There aren't integers")
else:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	
	suma = a + b
	resta = a - b
	product = a * b
	print("Sum:		", suma)
	print("Diference:	", resta)
	print("Product:	", product)
	if b == 0:
		print("Quotien:	ERROR (division by zero)")
		print("Rmainder:	ERROR (module by zero)")
	else:
		div = a / b
		mod = a % b
		print("Quotien:	", div)
		print("Rmainder:	", mod)
