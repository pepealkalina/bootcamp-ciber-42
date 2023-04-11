# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:06:12 by preina-g          #+#    #+#              #
#    Updated: 2023/04/11 20:42:25 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def text_analyzer(strin=""):
	"""
	This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	uppercase = 0
	lowercase = 0
	spaces = 0
	point_mark = 0

	if strin == "":
		print("What is the string for analyze?")
		ss = input(">> ")
		text_analyzer(ss)
	elif type(strin) != str:
		print("Error: The input is not a string")
	else:
		text = str(strin)
		text_len = len(text)
		i = 0
		while i < text_len:
			c = text[i]
			if c.isupper() == 1:
				uppercase += 1
			elif c.islower() == 1:
				lowercase += 1
			elif c.isspace() == 1:
				spaces += 1
			else:
				for j in string.punctuation:
					if c == j:
						point_mark += 1
			i += 1
		print("The text contains", text_len, "characters", )
		print("-", uppercase, "upper letter(s)")
		print("-", lowercase, "lower letter(s)")
		print("-", point_mark, "punctuations mark(s)")
		print("-", spaces, "space(s)")

if __name__=='__main__':
	argc = len(sys.argv)
	if argc >= 3:
		print("Error: More than one argument")
	elif argc == 1:
		text_analyzer()
	else:
		text_analyzer(sys.argv[1])

		