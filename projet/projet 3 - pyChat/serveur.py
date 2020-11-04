#coding utf-8
import threading
import socket


class ThreadForClient(threading.Thread):
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.conn = conn

	def run(self):
		print(conn)
		while True:
			data = self.conn.recv(1024)
			print(socket_objs[:])
			for msg in socket_objs:
				msg.sendall(data)
			data = data.decode("utf8")
			if not data:
				socket_objs.remove(conn)
				print("client deconnecter")
				conn.close()
				break

			print(data)
			if data == "deco()":
				print("client deconnecter")
				conn.close()
				break



#------------------------------------------------------------
host, port = ('', 5566)
socket_objs = []
serveur = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serveur.bind((host, port))
print("Le serveur est démarré..")

while True:
	serveur.listen(10)
	conn, adress = serveur.accept()
	pseudo = conn.recv(16)
	pseudo = pseudo.decode("utf8")
	print(f"{pseudo} viens de se connecter")
	socket_objs.append(conn)

	


	my_thread = ThreadForClient(conn)
	my_thread.start()

conn.close()
serveur.close()