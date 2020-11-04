#coding:utf-8

"""
condition -> - if <condition>: 
				<instructionsDeLaCondition>
			 <instructionHorsDeLaCondition>


			 - elif <autreCondition>:
			 	<instructionDeLaCondition>
			 <instructionHorsDeLaCondition>

			 - else: (sinon)

Opérateur de comparaison : == (égal à)
						   != (différent de)
						   < (plus petit que)
						   > (plus grand que)
						   <= (plus petit ou égal à)
						   >= (plus grand ou égal à)

Conditions multiple : and (ET)
					  or (OU)
					  in / not in (DANS / PAS DANS)


on peut également faire des condition avec des intervalle de la maniere : 

				if 0 < {VARIABLE} <= 100: (exemple ligne 50)
"""

age = int(input("Entre ton age : "))

if age == 18:
	print("tu es majeur !")
elif age < 18:
	print("tu es petit")
	print("tu as {} ans".format(age))
else:
	print("tu es grand")
	print("tu as {} ans".format(age))

lettre_hasard = "b"

if lettre_hasard in "aeiouy":
	print("c'est une voyelle")
else:
	print("c'est une consonne")

intervalle = int(input("entre un nbre entre 0 et 100 : "))

if 0 <= intervalle <= 100 : #intervalle de 0 à 100
	print("nbre validé")
else:
	print("nbre refusé")
	

