#!/usr/bin/python3

'''	Simple script to check host response when sending a payload.
	by TransparentHat	
	Telegram: @SzMrts
'''

import os
import socket
import sys

try:
	target_host = str(sys.argv[1])
	target_port = int(sys.argv[2])
	target_get = str(sys.argv[3])
	
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((target_host, target_port))

	payload = "GET " + target_get + " HTTP/1.1\r\nHost: " + target_host + "/\r\nConnection: Keep-alive\n\r\n"

	client.send(payload.encode(encoding='utf-8'))

	response = client.recv(4096)

	print(response.decode('utf-8'))

except IndexError:
	
	print('\n \033[1;32mUsage: ./paytest [host] [port] [get] \n')
