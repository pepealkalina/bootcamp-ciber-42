# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 12:56:38 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 16:57:09 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

arg_len = len(sys.argv)

if arg_len == 1:
	exit()
else:
	i = arg_len - 1;
	while i >= 1:
		argv = str(sys.argv[i]) [::-1]
		if i == 1:
			print(argv.swapcase())
		else:
			print(argv.swapcase(), end = " ")
		i -= 1