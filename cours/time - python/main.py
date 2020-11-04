#coding:utf-8
import time



"""
begin = time.time()
print("Début")

time.sleep(5)

end = time.time()
print("Fin")
print("le programme est resté allumer {} secondes".format(end-begin))
"""

tps = time.localtime()
print(tps)


print(time.strftime("%d/%m/%Y")) # %Z -> fuseau horaire 

