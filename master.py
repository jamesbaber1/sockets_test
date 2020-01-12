import time
import sys
import socket
import os

master_socket = socket.socket()
host = socket.gethostname()
print(host)
port = 8080

master_socket.bind((host, port))
print('')
print('Waiting for  connections...')
print('')

master_socket.listen(1)
connection, address = master_socket.accept()

print('')
print(address, ' has connected to the server')
print('')