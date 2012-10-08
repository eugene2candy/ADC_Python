#! /usr/bin/python
import sys
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------------
#		Script de parcours en profondeur d'un arbre (Depth First Search)
#			et de parcours en largeur (Breadth First Search)
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

#On definit DICO_ARBRE : dictionnaire contenant les noeuds et leurs noeuds adjacents
DICO_ARBRE=dict()

#-----------------------Lecture du fichier et sauvegarde des donnees dans le dictionnaire----------------------------
#On lit la premiere ligne du fichier et on la stocke dans la variable l
l=fic_arbre.readline()

#On separe la ligne l apres les espaces ; l devient une liste 
l=l.split()

#On assigne le premier element de la liste l a s0
s0=int(l[0])

#Tant que le fichier n'est pas vide
while l :
	#Si le noeud considere a des fils, ie si la ligne contient plus d'un element
	if (len(l)>1) :
		#Si le noeud est deja present dans le dictionnaire
		if(DICO_ARBRE.has_key(int(l[0])) == True) : 
			#On met a jour la liste de ses fils
			DICO_ARBRE[int(l[0])]=DICO_ARBRE[int(l[0])]+","+l[1]
		#Sinon on insere le noeud dans le dictionnaire et on lui associe son fils		
		else :
			DICO_ARBRE[int(l[0])]=l[1]
	#Si le noeud considere n'a pas de fils
	else :
		if(DICO_ARBRE.has_key(int(l[0])) == False) :
			#On lui associe un espace dans le dictionnaire
			DICO_ARBRE[int(l[0])]=" "
	#On lit la ligne suivante du fichier
	l=fic_arbre.readline()
	#On separe la ligne selon les espaces
	l=l.split()

#-----------------------Fonction de parcours en profondeur de l'arbre----------------------------
def parcoursProfondeur(s0,DICO_ARBRE) :
	print "Parcours en profondeur"
	#Etape 1 : On place le sommet initial s0 dans OUVERT
	OUVERT.append(s0)
	#Tant que la liste OUVERT n'est pas vide
	while OUVERT :
		#Soit n le premier element de la liste OUVERT
		n=OUVERT[0]
		#l est la liste des fils de n, stockee dans DICO_ARBRE
		l=DICO_ARBRE[n]
		#Si n a des fils = si l a plus d'un element
		if (len(l)>1) :
			#On separe l apres les virgules
			l2=l.split(",")
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
		#On affiche n a l'ecran
		print n 
		#On cherche le nouvel indice de n dans la liste OUVERT
		indice_n=OUVERT.index(n)
		#On supprime n de OUVERT
		OUVERT.pop(indice_n)

#-----------------------Fonction de parcours en largeur de l'arbre----------------------------
def parcoursLargeur(s0,DICO_ARBRE) :
	print "Parcours en largeur"
	#Etape 1 : On place le sommet initial s0 dans OUVERT
	OUVERT.append(s0)
	#Tant que la liste OUVERT n'est pas vide
	while OUVERT :
		#Soit n le premier element de la liste OUVERT
		n=OUVERT[0]
		#l est la liste des fils de n, stockee dans DICO_ARBRE
		l=DICO_ARBRE[n]
		#Si n a des fils = si l a plus d'un element
		if (len(l)>1) :
			#On separe l apres les virgules
			l2=l.split(",")
			#Tant que l2 n'est pas vide = tant que n a des fils
			while l2 :
				#On met les fils de n en tete d'OUVERT
				OUVERT.append(int(l2[0]))
				#On supprime les fils de l2
				l2.pop(0)
		#On effectue le traitement de n = on ecrit n dans le fichier resultats
		fic_res.write(str(n))
		#On met n dans FERME
		FERME.append(n)
		#On affiche n a l'ecran
		print n 
		#On cherche le nouvel indice de n dans la liste OUVERT
		indice_n=OUVERT.index(n)
		#On supprime n de OUVERT
		OUVERT.pop(indice_n)

#On execute les fonctions
parcoursProfondeur(s0,DICO_ARBRE)
parcoursLargeur(s0,DICO_ARBRE)

#On ferme les fichiers
fic_arbre.close()
fic_res.close()



