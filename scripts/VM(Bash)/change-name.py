#!/usr/bin/env python3
import os
import sys
import subprocess

filename=sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        newline = line.strip().replace("jane", "jdoe")
        subprocess.run(["mv", line.strip(),newline])
f.close()
