#! /usr/bin/python
import sys
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------------
#		Script de parcours en profondeur d'un arbre (Depth First Search)
#------------------------------------------------------------------------------------------------

#Le fichier donne en parametre 1 contient la structure d'un arbre sous forme de liste adjacente
fichier_arbre=sys.argv[1]

#Le fichier donne en parametre 2 est le fichier resultat
fichier_resultat=sys.argv[2]

#On ouvre le fichier fichier_arbre en lecture
try:                     		
	fic_arbre = open(fichier_arbre,'r')
except IOError, e:      		
	print "Fichier inconnu: ", fichier_arbre

#On ouvre le fichier fichier_resultat en ecriture
try:                     		
	fic_res = open(fichier_resultat,'w')
except IOError, e:      		
	print "Fichier inconnu: ", fichier_resultat

#On definit la liste OUVERT : liste d'attente contenant les sommets en attente
OUVERT = list()

#On definit la liste FERME : liste contenant les sommets dont les successeurs ont deja ete enumeres
FERME = list() 

#On lit la premiere ligne du fichier et on la stocke dans la variable l
l=fic_arbre.readline()

#La premiere ligne, stockee dans la variable l, correspond au nombre total de noeuds de l'arbre
nb_noeuds=int(l)

#On lit la ligne suivante du fichier
l=fic_arbre.readline()

#On separe la ligne l apres les tabulations ; l devient une liste 
l=l.rsplit("\t")

#On assigne le premier element de la liste l a s0
s0=int(l[0])

#Etape 1 : On place le sommet initial s0 dans OUVERT
OUVERT.append(s0)

#Tant que le fichier n'est pas vide
while OUVERT :
	#print OUVERT
	#On calcule la taille de la liste l
	taille_l=len(l)
	#Soit n le premier element de la liste OUVERT
	n=OUVERT[0]
	print n
	#Si n a des fils = si l a plus d'un element
	if (taille_l>1) :
		#On stocke l en ayant supprime les parentheses et le retour a la ligne dans l2
		l2=l[1].replace("(",'')
		l2=l2.replace(')','')
		l2=l2.replace('\n','')
		#On separe l2 apres les virgules
		l2=l2.split(",")
		#Tant que l2 n'est pas vide = tant que n a des fils
		while l2 :
			#On met les fils de n en tete d'OUVERT
			OUVERT.insert(0,int(l2[0]))
			#On supprime les fils de l2
			l2.pop(0)
	#On effectue le traitement de n = on ecrit n dans le fichier resultats
	fic_res.write(str(n))
	#On met n dans FERME
	FERME.append(n)
	#On cherche le nouvel indice de n dans la liste OUVERT
	indice_n=OUVERT.index(n)
	print OUVERT
	#On supprime n de OUVERT
	OUVERT.pop(indice_n)
	print OUVERT
	#On lit la ligne suivante du fichier
	l=fic_arbre.readline()
	#On separe la ligne l apres les tabulations 
	l=l.rsplit("\t")

#On ferme les fichiers
fic_arbre.close()
fic_res.close()
print FERME



