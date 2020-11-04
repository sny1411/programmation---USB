#coding:utf-8
import sqlite3

try:
	connection = sqlite3.connect("base.db")
	cursor = connection.cursor()

	req = cursor.execute('SELECT * FROM t_users')

	for row in req.fetchall():
		print(row[1])
except Exception as e:
	print("[ERREUR]", e)
	connection.rollback()
finally:
	connection.close()



"""new_user = (cursor.lastrowid, "Julie", 23)
cursor.execute('INSERT INTO t_users VALUES(?,?,?)',new_user)
connection.commit()
print("Nouvel utilisateur ajouter")"""
#cursor.executemany() -> pour ajouter plusieur choses en meme temps






