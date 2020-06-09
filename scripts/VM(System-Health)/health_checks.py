#!/usr/bin/env python3
import shutil
import psutil

from network import *

def check_disk_usage(disk):
    du = shutul.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print("System CPU and disk OK")

elif check_localhost() and check_connectivity():
    print("System and Network OK")

else:
    print("Network Check FAILURE")
