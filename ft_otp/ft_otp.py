# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/21 13:18:02 by preina-g          #+#    #+#              #
#    Updated: 2023/05/12 13:52:16 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import hmac
import hashlib
import time 
import string
import os
import argparse
import pyotp
import base64
from cryptography.fernet import Fernet

def get_otp_key(key_file):
    with open(key_file, 'rb') as file:
        decrypt_key = open('decrypt.key', 'rb').read()
        decode = Fernet(decrypt_key)
        key = decode.decrypt(file.read())
        time_code = int(time.time())//30 #genera el codigo de tiempo para luego generar el codigo encriptado
        code = hmac.new(bytearray.fromhex(str(key).split("'")[1]) , int.to_bytes(time_code, 8, byteorder='big'), hashlib.sha1).digest()
        nibble = code[len(code) - 1] & \xf #extrae  el ultimo semi-octeto (nibble) del codigo hmac 
        otp_pass = (	#convierte el nibble en  el codigo de 6 cifras
            (code[nibble] & \x7f) << 24 |
            (code[nibble + 1] & \xff) << 16 |
            (code[nibble + 2] & \xff) << 8 |
            (code[nibble + 3] & \xff)) % 1000000
        print("OTP password: {:06d}".format(otp_pass))#imprime el otp y si hay menos dde 6 cifras las rellena con 0

#Encripta la clave en un archivo ft_otp.key
def encrypt_key(hex_key):
    print('Creatin ft_otp.key ...')
    with open('ft_otp.key', 'w') as file:
        file.write(hex_key)
    key_c = Fernet.generate_key()#clave desencriptar
    with open('decrypt.key', 'wb') as decrypt:
        decrypt.write(key_c)
    with open('ft_otp.key', 'rb') as si:
        alcachofas = si.read()
    cipher = Fernet(key_c)
    en_key = cipher.encrypt(alcachofas)
    with open('ft_otp.key', 'wb') as no:
        no.write(en_key)
    print('ft_otp.key DONE!')
    
#Coge la clave hexadecimal de argumento
def get_hex_key(hex_key):
    if len(hex_key) >= 64 and all(n in string.hexdigits for n in hex_key):
        encrypt_key(hex_key)
    elif os.path.isfile(hex_key): #comprueba que si no se le pasa directamente haya un archivo con esta.
        with open(hex_key, 'r') as file:
            hexa = file.read()
            get_hex_key(hexa)
    else:
        print('ERROR: key must be 64 hexadecimal characters or an archive that contais that')

def test():
    print('Esto es un test para verificar que la otp key que genero es igual a la de PyOTP', end='\n\n')
    hexa = '686f6c61207175652074616c20657374616973206d756e646f20637275656565656565656c'
    base32 = 'NBXWYYJAOF2WKIDUMFWCAZLTORQWS4ZANV2W4ZDPEBRXE5LFMVSWKZLFMVWA===='
    otp1 = pyotp.TOTP(base32)
    get_otp_key('ft_otp.key')
    print('PyOTP key:',otp1.now())

def argument_parser():
    parser = argparse.ArgumentParser(description='Generador de claves OTP a travves de una clave hexadecimal de 64 caracteres')
    parser.add_argument('-g', '--generate', type=str, help='Create a ft_otp.key file')
    parser.add_argument('-k', '--key', type=str, help='Generates a OTP key')
    parser.add_argument('-t', '--test', action='store_true', help='Test ft_otp with pyotp')
    return parser
    
if __name__=='__main__':
    args = argument_parser().parse_args()
    parser = argument_parser()
    if args.generate:
        get_hex_key(args.generate)
    elif args.key:
        if os.path.isfile(args.key) and str(args.key).endswith('ft_otp.key'):
            get_otp_key(args.key)
        else:
            print('ERROR: The key file must be ft_otp.key')
    elif args.test:
        test()
    else:
        parser.print_help()
    