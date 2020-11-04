#coding:utf-8
import socket
import time

host, port = ('127.0.0.1', 5566)

try:
	socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	socket.connect((host, port))
	print("client connecté !")
	
	while True:
		time.sleep(1)
		data = str(input(">>> "))
		data = data.encode("utf8")
		socket.sendall(data)
		if data == 
except:
	print("connexion au serveur échouée !")
finally:
	socket.close()