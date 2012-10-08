#! /usr/bin/python
import sys
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------------------------
#		Script de parcours en profondeur d'un graphe (Depth First Search)
#			et de parcours en largeur (Breadth First Search)
#------------------------------------------------------------------------------------------------

#Le fichier donne en parametre 1 contient la structure d'un graphe sous forme de liste adjacente
fichier_graphe=sys.argv[1]

#Le fichier donne en parametre 2 est le fichier resultat
fichier_resultat=sys.argv[2]

#On ouvre le fichier fichier_graphe en lecture
try:                     		
	fic_graphe = open(fichier_graphe,'r')
except IOError, e:      		
	print "Fichier inconnu: ", fichier_graphe

#On ouvre le fichier fichier_resultat en ecriture
try:                     		
	fic_res = open(fichier_resultat,'w')
except IOError, e:      		
	print "Fichier inconnu: ", fichier_resultat

#On definit la liste OUVERT : liste d'attente contenant les sommets en attente
OUVERT = list()

#On definit la liste FERME : liste contenant les sommets dont les successeurs ont deja ete enumeres
FERME = list() 

#On definit DICO_graphe : dictionnaire contenant les noeuds et leurs noeuds adjacents
DICO_graphe=dict()

#On definit DICO_visite : dictionnaire indiquant si les noeuds ont ete visites
DICO_visite=dict()

#-----------------------Lecture du fichier et sauvegarde des donnees dans le dictionnaire----------------------------
#On lit la premiere ligne du fichier et on la stocke dans la variable l
l=fic_graphe.readline()

#On separe la ligne l apres les espaces ; l devient une liste 
l=l.split()

#On cree la variable nombre_noeuds qui contiendra le nombre total de noeud du graphe
nombre_noeuds=0 

#Tant que le fichier n'est pas vide
while l :
	#Si le noeud considere a des successeurs, ie si la ligne contient plus d'un element
	if (len(l)>1) :
		#Si le noeud est deja present dans le dictionnaire
		if(DICO_graphe.has_key(int(l[0])) == True) : 
			#On met a jour la liste de ses successeurs
			DICO_graphe[int(l[0])]=DICO_graphe[int(l[0])]+","+l[1]
			if(DICO_graphe.has_key(l[1]) == False) :
				nombre_noeuds+=1
		#Sinon on insere le noeud dans le dictionnaire et on lui associe son successeur		
		else :
			DICO_graphe[int(l[0])]=l[1]
			nombre_noeuds+=1
			if(DICO_graphe.has_key(l[1]) == False) :
				nombre_noeuds+=1
	#Si le noeud considere n'a pas de successeurs
	else :
		if(DICO_graphe.has_key(int(l[0])) == False) :
			#On lui associe un espace dans le dictionnaire
			DICO_graphe[int(l[0])]=" "
			nombre_noeuds+=1
	#On lit la ligne suivante du fichier
	l=fic_graphe.readline()
	#On separe la ligne selon les espaces
	l=l.split()
	print DICO_graphe
	print nombre_noeuds
#-----------------------Fonction de parcours en profondeur du graphe----------------------------
def parcoursProfondeur(DICO_graphe,DICO_visite) :
	#On initialise la variable nb_composantes a 0
	nb_composantes=0
	print "Parcours en profondeur"	
	#Pour tous les noeuds i
	for i in range(nombre_noeuds) :
		#Si le noeud i n'a pas ete visite
		if(DICO_visite.has_key(i) == False) :
			#On incremente le nombre de composantes
			nb_composantes+=1
			#i est le sommet initial
			s0=i
			#Etape 1 : On place le sommet initial s0 dans OUVERT
			OUVERT.append(s0)
			#On marque s0 comme visite
			DICO_visite[s0]=1
			#Tant que la liste OUVERT n'est pas vide
			while OUVERT :
				#Soit n le premier element de la liste OUVERT
				n=OUVERT[0]
				#On retire n de OUVERT
				OUVERT.pop(0)
				#l est la liste des successeurs de n, stockee dans DICO_graphe
				if(DICO_graphe.has_key(n) == False) :
					l=''
				else :
					l=DICO_graphe[n]
				#Si n a des successeurs = si l a plus d'un element
				if (len(l)>=1) :
					#On separe l apres les virgules
					l2=l.split(",")
					#Tant que l2 n'est pas vide = tant que n a des successeurs
					while l2 :
						#Si les successeurs n'ont pas ete visites
						if(DICO_visite.has_key(int(l2[0])) == False) :
							#On met les successeurs de n en queue d'OUVERT
							OUVERT.insert(0,int(l2[0]))
							#On les marque come visites
							DICO_visite[int(l2[0])] = 1
						#On supprime les successeurs de l2
						l2.pop(0)
				#On effectue le traitement de n = on ecrit n dans le fichier resultats
				fic_res.write(str(n))
				#On met n dans FERME
				FERME.append(n)
				#On affiche n a l'ecran
				print n 
	return nb_composantes
				

#-----------------------Fonction de parcours en largeur du graphe----------------------------
def parcoursLargeur(DICO_graphe,DICO_visite) :
	#On initialise la variable nb_composantes a 0
	nb_composantes=0
	print "Parcours en largeur"	
	#Pour tous les noeuds i
	for i in range(nombre_noeuds) :
		#Si le noeud i n'a pas ete visite
		if(DICO_visite.has_key(i) == False) :
			#On incremente le nombre de composantes
			nb_composantes+=1
			#i est le sommet initial
			s0=i
			#Etape 1 : On place le sommet initial s0 dans OUVERT
			OUVERT.append(s0)
			#On marque s0 comme visite
			DICO_visite[s0]=1
			#Tant que la liste OUVERT n'est pas vide
			while OUVERT :
				#Soit n le premier element de la liste OUVERT
				n=OUVERT[0]
				#On retire n de OUVERT
				OUVERT.pop(0)
				#l est la liste des successeurs de n, stockee dans DICO_graphe
				if(DICO_graphe.has_key(n) == False) :
					l=''
				else :
					l=DICO_graphe[n]
				#Si n a des successeurs = si l a plus d'un element
				if (len(l)>=1) :
					#On separe l apres les virgules
					l2=l.split(",")
					#Tant que l2 n'est pas vide = tant que n a des successeurs
					while l2 :
						#Si les successeurs n'ont pas ete visites
						if(DICO_visite.has_key(int(l2[0])) == False) :
							#On met les successeurs de n en queue d'OUVERT
							OUVERT.append(int(l2[0]))
							#On les marque come visites
							DICO_visite[int(l2[0])] = 1
						#On supprime les successeurs de l2
						l2.pop(0)
				#On effectue le traitement de n = on ecrit n dans le fichier resultats
				fic_res.write(str(n))
				#On met n dans FERME
				FERME.append(n)
				#On affiche n a l'ecran
				print n 
	return nb_composantes
				

#On execute les fonctions
nb_composantes=parcoursProfondeur(DICO_graphe,DICO_visite)
print "Le graphe possede "+str(nombre_noeuds)+" noeuds et "+str(nb_composantes)+" composantes."
nb_composantes=parcoursLargeur(DICO_graphe,DICO_visite)
print "Le graphe possede "+str(nombre_noeuds)+" noeuds et "+str(nb_composantes)+" composantes."


#On ferme les fichiers
fic_graphe.close()
fic_res.close()



