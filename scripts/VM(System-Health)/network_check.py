#!/usr/bin/env python 3
import requests
import socket

def check_localhost():
    if localhost == "127.0.0.1":
        return True
    return False

def check_connectivity():
    if response == 200:
        return True
    return False

localhost = socket.gethostbyname('localhost')
check_localhost()

req = requests.get("http://www.google.com")
res = req.status_code
check_connectivity()
