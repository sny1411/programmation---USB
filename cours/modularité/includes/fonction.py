#coding:utf-8

def dire(nom_personne="sa MAMAN", message_personne="SALUT"):
	print("{} : {}".format(nom_personne,message_personne))

test = lambda : print("test")

if __name__ == "__main__":
	test()
	dire()