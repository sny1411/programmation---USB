#coding:utf-8
import socket
import threading

def donneSend():
	
	print("ThreadSend running !")
	while True:
		
		data_msg = str(input(">>> "))
		if data_msg == "deco()":
			gotoserver(data_msg)
			print("au revoir..")
			break
		gotoserver(data_msg)

def donneGet():
	print("ThreadGet running !")
	while True:
			
			data = socket.recv(1024)
			data = data.decode("utf8")
			print(data)
			if not data:
				print("probleme avec le serveur :(")
				conn.close()
				break


def gotoserver(data):
	data = data.encode("utf8")
	socket.sendall(data)

host, port = ('127.0.0.1', 5566)


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host, port))
print("client connecté !")
pseudo = str(input("entre ton pseudo stp -> "))
gotoserver(pseudo)
threadSend = threading.Thread(target=donneSend)
threadGet = threading.Thread(target=donneGet)

threadSend.start()
threadGet.start()


threadGet.join()
threadSend.join()
	
socket.close()