#coding:utf-8
import datetime

date1 = datetime.datetime(2020, 6, 27)
print(date1)

date2 = datetime.datetime(2020, 5, 26)

if date1 < date2:
	print("d2 plus ancien")
else:
	print("d1 plus récent")

date3 = datetime.date(2020,5,26)
print(date3)

"""
date.year() -> recupere année d'une date instancié

"""
from datetime import datetime

print(datetime.now())