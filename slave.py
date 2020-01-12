import time
import sys
import socket
import os

slave_socket = socket.socket()
host = 'DESKTOP-6SB7IPL'
port = 8080

slave_socket.connect((host, port))
print('')
print('Connected to server!')
