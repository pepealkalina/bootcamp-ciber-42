# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 20:41:23 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 16:46:56 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def guess_num(num, count, guess=""):
	if guess == "":
		print("Invalid expression")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	if str(guess) == "exit":
		print("Goodbye!")
		exit()
	elif guess.isnumeric() == False:
		print("Invalid expression")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	elif int(guess) >= 100:
		print("Out of range")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	elif int(guess) <= 0:
		print("Out of range")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	elif int(guess) < num:
		print("Too Low!")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	elif int(guess) > num:
		print("Too Higth!")
		count += 1
		guess_num(num, count, input("Guess the number:\n>>> "))
	elif int(guess) == num and int(guess) == 42:
		print("correct number!")
		print("The answer to the ultimate question of life, the universe and everything is 42.")
		if count == 0:
			print("Congratulations! You got it on your first try!")
		else:
			print("You won in {} attempts!".format(count))
		exit()
	elif int(guess) == num:
		print("correct number!")
		if count == 0:
			print("Congratulations! You got it on your first try!")
		else:
			print("You won in {} attempts!".format(count))
		exit()
	
	

if __name__=='__main__':
    number = random.randint(1, 99)
    count = 0
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    guess_num(number, count, input("Guess the number:\n>>> "))
    