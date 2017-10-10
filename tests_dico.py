ville={'david': 'Rouen', 'laurent' : 'Versailles' , 'yann' : 'Paris' }
print 'le dico :' ,ville
print 'ses codes : ', ville.keys()
print 'ses valeurs : ', ville.values()
print ' sa longueur : ', len(ville)

print 'rentrez un nom'
a=raw_input()
if a in ville :
	print ville[a]
else :
	print 'quelle est sa ville ?'
	b=raw_input()
	ville[a]=b
	
print ville

for cle in ville:
	print 'la ville de ', cle, 'est ', ville[cle]
	
	
	

