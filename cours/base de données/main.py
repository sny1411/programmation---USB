#coding:utf-8
import sqlite3

#CRUD : create,read,update,delete
connection = sqlite3.connect("base.db")
cursor = connection.cursor()

my_username = ("SNY",)
cursor.execute('SELECT * FROM t_users WHERE user_name = ?', my_username)

print(cursor.fetchone()[2])

connection.close()