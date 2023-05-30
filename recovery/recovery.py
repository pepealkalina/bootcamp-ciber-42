# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recovery.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/19 11:42:25 by preina-g          #+#    #+#              #
#    Updated: 2023/05/30 13:56:28 by preina-g         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import winreg
from datetime import datetime, timedelta
import psutil
import sqlite3
import wmi
import win32com.client
import argparse

default_time = datetime.now() - timedelta(days = 1)

def branches_change_date():
    #types of regystry to analyze\
    path = r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
    keys = [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]
    try:
        for key in keys:
            #open the registry key
            key1 = winreg.OpenKey(key, path)
            #get timestamp
            timestamp = winreg.QueryInfoKey(key)[2] / 10000000 - 11644473600
            date = datetime.fromtimestamp(timestamp)
            if default_time <= date <= datetime.now():
                print("Last modify: {} --- Current Version Run: {}".format(date.strftime("%Y-%m-%d %H:%M:%S") ,key1))
            else:
                print("There are not changes in this registry key in current date")
    except:
        pass

def recent_files():
    #Recent used/opened files
    r_files_path = os.path.expanduser('~\\AppData\\Roaming\\Microsoft\\Windows\\Recent')
    for files in os.listdir(r_files_path):
        if not files.endswith('.lnk'):
            continue
        else:
            path = os.path.join(r_files_path, files)
            mod_date = datetime.fromtimestamp(os.path.getmtime(path))
            if default_time <= mod_date <= datetime.now():
                print('File: {} \n-- Modification Date: {}\n'.format(files.strip('.lnk'), mod_date.strftime("%Y-%m-%d %H:%M:%S")))

def instaled_programs():
    instaled_programs = 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall'
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, instaled_programs)
    for i in range( winreg.QueryInfoKey(key)[0]):
        try:
            keyname = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, keyname)
            install_date = winreg.QueryValueEx(subkey, "InstallDate")[0]
            if default_time <= datetime.strptime(install_date, "%Y%m%d") <= datetime.now():
                print("Install Date: {} -- Program: {}".format(datetime.strptime(install_date, "%Y%m%d"), winreg.QueryValueEx(subkey, "DisplayName")[0]))
        except FileNotFoundError:
            try:
                keyname = winreg.EnumKey(key, i)
                subkey = winreg.OpenKey(key, keyname)
                if default_time <= datetime.now():
                    print("No install Date -- Program: {}".format(winreg.QueryValueEx(subkey, "DisplayName")[0]))
            except FileNotFoundError:
                pass


def proccess_in_exec():
    proccess_in_exec = psutil.process_iter(['pid', 'name', 'create_time'])
    for proccess in proccess_in_exec:
        create_time = datetime.fromtimestamp(proccess.create_time()).strftime("%Y-%m-%d %H:%M:%S")
        time_format = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S")
        if default_time <= time_format <= datetime.now():
            print("PID: {} -- {} -- Create Time: {}".format(proccess.pid , proccess.name(), time_format))

def get_browser_history(path, name):
    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        if name == 'chrome':
            try:
                cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
            except:
                print("Error to get the browser history from Chrome")
        elif name == 'firefox':
            try:
                cursor.execute("SELECT url, title, visit_count, last_visit_time FROM moz_places")
            except:
                print("Error to get the browser history from Firefox")
        elif name == 'edge':
            try:
                cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
            except:
                print("Error to get the browser history from Edge")
        
        results = cursor.fetchall()
        for result in results:
            print("URL: {} -- Title: {} -- Visit Count: {} -- Last Visit Time: {}".format(result[0], result[1], result[2], datetime.fromtimestamp(result[3]/1000000 - 11644473600).strftime("%Y-%m-%d %H:%M:%S")))
    except:
        print(f"Error to connect to database, is not possible to get the browser history from {name}")
    


def browser_history():
    #Chrome
    chrome_path = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
    get_browser_history(chrome_path, 'chrome')
    #Firefox
    firefox_path = os.path.expanduser('~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\')
    get_browser_history(firefox_path, 'firefox')
    #Edge
    edge_path = os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History')
    get_browser_history(edge_path, 'edge')
    

def remote_connections():
    connections = psutil.net_connections(kind='inet')
    for connection in connections:
        if connection.status == psutil.CONN_ESTABLISHED:
            if default_time <= datetime.fromtimestamp(connection.raddr.port) <= datetime.now():
                print("Remote IP: {} -- Remote Port: {} -- Status: {}".format(connection.raddr.ip, connection.raddr.port, connection.status))

def connected_devices():
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_USBHub"):
        print("USB: {} -- Description: {} -- Device ID: {}".format(usb.Name, usb.Description, usb.DeviceID))
    print("\n---- Remote Connections ----", end='\n\n')
    remote_connections()
    

def evets_log():
    l = wmi.WMI()
    name = 'System'
    logs = l.Win32_NTLogEvent(Logfile=name)
    for log in logs:
        if default_time <= datetime.strptime(log.TimeGenerated.split(".")[0], '%Y%m%d%H%M%S') <= datetime.now():
            try:
                print("Event Code: {} \n Type: {} \n Source: {} \n Time Generated: {} \n Message: {}".format(log.EventCode, log.Type, log.SourceName, datetime.strptime(log.TimeGenerated.split(".")[0], '%Y%m%d%H%M%S'), log.Message), end='\n\n')
            except UnicodeEncodeError:
                pass

def manage_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        return date
    except:
        print("Error to convert the date, please try again")
        return None

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', help='Date to analyze in format YYYY-MM-DD', type=manage_date)
    args = parser.parse_args()
    return args


def main():
    global default_time
    if parse_args().date:
        default_time = parse_args().date
    
    print("---- Braches changes date ----", end='\n\n')
    branches_change_date()
    print("\n---- Recents Files ----", end='\n\n')
    recent_files()
    print("\n---- Instaled Programs ----", end='\n\n')
    instaled_programs()
    print("\n---- Proccess in execution ----", end='\n\n')
    proccess_in_exec()
    print("\n---- Browser History ----", end='\n\n')
    browser_history()
    print("\n---- Connected Devices ----", end='\n\n')
    connected_devices()
    print("\n---- Events Log ----", end='\n\n')
    evets_log()

main()