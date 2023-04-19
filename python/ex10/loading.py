# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 09:55:46 by preina-g          #+#    #+#              #
#    Updated: 2023/04/13 21:23:13 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

def print_bar(num, loaded, init1):
    if num == 0:
        x = 30
        percentage = 100
    else:
        x = int(30*loaded/num)
        percentage = round(100*loaded/num) 
    et = time.time() - init1
    if et == 0:
        speed = 0
    else:
        speed = (loaded/et)
    if speed == 0:
        eta = 0
    else:
        eta = (num/speed)
    if x == 30:
        print("ETA: {:.2f}s [{:>3}%][{}{:>}{}] {}/{} elapsed time {:.2f}s".format(eta, percentage,"="*x, "=", " "*(30-x), loaded, num, et), end="\r")
    else:
        print("ETA: {:.2f}s [{:>3}%][{}{:>}{}] {}/{} elapsed time {:.2f}s".format(eta, percentage, "="*x, ">", " "*(30-x), loaded, num, et), end="\r")

def ft_progress(listy):
    init = time.time()
    num1 = len(listy)
    print_bar(num1, 0, init)
    for i, load in enumerate(listy):
        yield load
        i += 1
        print_bar(num1, i, init)
        
        

if __name__=='__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print("\n...")
    print(ret, end="\n\n")
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.005)
    print("\n...")
    print(ret)
