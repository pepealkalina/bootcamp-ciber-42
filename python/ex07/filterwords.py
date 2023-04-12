# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 13:47:24 by preina-g          #+#    #+#              #
#    Updated: 2023/04/12 16:14:21 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def filter_words(arg1, arg2):
	strin = arg1.split()
	num = int(arg2)
	words = [word for word in strin if len(word) > num]
	filtered = []

	i = 0;
	while i < len(words):
		count = 0
		for j in string.punctuation:
			for chara in str(words[i]):
				if chara != j:
					count += 1
		for j in string.punctuation:
			for chara in str(words[i]):
				if chara == j:
					words[i] = words[i].replace(chara, '')
		if count >= num:
			filtered.extend([words[i]])
		i += 1
	print(filtered)				

if __name__=='__main__':
	
	argc = len(sys.argv)
	if argc != 3:
		print("ERROR")
	elif sys.argv[1].isnumeric() == True or sys.argv[2].isnumeric() == False:
		print("ERROR")
	else:
		arg1 = sys.argv[1]
		arg2 = sys.argv[2]
		filter_words(arg1, arg2)