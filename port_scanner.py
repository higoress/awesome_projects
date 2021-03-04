#!/usr/bin/python3

''' 
Simple port scanner using only standard lib
@author: Higor Emanuel Souza Silva
@contact: www.github.com/higoress
@license: MIT
'''

import argparse
from datetime import datetime
import socket
import sys


def check_ip_format(ip: str) -> str:
    ip_parts = ip.split('.')
    if len(ip_parts) != 4:
        print("[ERROR] Wrong IPv4 Address format")
        sys.exit(-1)
    for part in ip_parts:
        int_part = int(part)
        if not (0 <= int_part <= 255):
            print("[ERROR] Invalid IPv4 Address")
            sys.exit(-1)
    return ip


parser = argparse.ArgumentParser(description="Simple Port Scanner", epilog="made by 0xXx")
parser.add_argument("host", type=check_ip_format)
args = parser.parse_args()
target_host = socket.gethostbyname(args.host)
start_time = datetime.now()
print("*"*64)
print(f"Scanning: {target_host}")
print("*"*64)

try:
    for port in range(1,1000):
        socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_handler.settimeout(1)
        connection_status = socket_handler.connect_ex((target_host, port))
        if connection_status is 0:
            print(f"Port {port} is open.")
        socket_handler.close()
    print("*"*64)
    print(f"total elapsed time: {datetime.now() - start_time} seconds")
except KeyboardInterrupt:
    print("[CANCEL] Exiting Program")
    sys.exit(-1)
except socket.gaierror:
    print("[ERROR] Hostname could not be resolved.")
    sys.exit(-1)
except socket.error:
    print("[ERROR] Couldn't connect to the server.")
    sys.exit(-1)




