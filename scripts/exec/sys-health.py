#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
    du = shutul.disk_usage(disk)
    free = du.free / du.total * 100
    return free

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage

print(check_disk_usage("/"))
print(check_cpu_usage())
