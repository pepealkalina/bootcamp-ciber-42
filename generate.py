# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generate.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/10 11:31:32 by preina-g          #+#    #+#              #
#    Updated: 2023/05/12 16:09:43 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import random

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

i = 0

while i <= 1000:
    file = '/Users/preina-g/infection/' + str(i) + random.choice(wannacry)
    os.system(f'touch {file}')
    i += 1