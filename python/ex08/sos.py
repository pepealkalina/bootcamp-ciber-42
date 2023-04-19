# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:35:25 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 19:00:41 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_dict = {
    'A' : '.-', 'B' : '-...', 'C' : '-.-.',
    'D' : '-..', 'E' : '.', 'F' : '..-.',
    'G' : '--.', 'H' : '....', 'I' : '..',
    'J' : '.---', 'K' : '-.-', 'L' : '.-..',
    'M' : '--', 'N' : '-.', 'O' : '---',
    'P' : '.--.', 'Q' : '--.-', 'R' : '.-.',
    'S' : '...', 'T' : '-', 'U' : '..-',
    'V' : '...-', 'W' : '.--', 'X' : '-..-',
    'Y' : '-.--', 'Z' : '--..', '0' : '-----',
    '1' : '.----', '2' : '..---', '3' : '...--',
    '4' : '....-', '5' : '.....', '6' : '-....',
    '7' : '--....', '8' : '---..', '9' : '----.',
    ' ' : '/'
}

def traduce_to_morse(joined):
    i = 0
    morse = []
    while i < len(joined):
        c = joined[i]
        if c.isalnum() == 1 or c.isspace() == 1:
            morse.append(morse_dict[c.upper()])
        else:
            print("ERROR")
            exit()
        i += 1
    morse = ' '.join(morse)
    print(morse)

    

if __name__=='__main__':
    if len(sys.argv) < 2:
        exit()
    else:
        joined = ' '.join(sys.argv[1:])
        traduce_to_morse(joined)
